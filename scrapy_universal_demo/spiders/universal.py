from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from .. import utils
from ..items import item_class_factory
from ..loaders import loader_factory


class UniversalSpider(CrawlSpider):
    name = "universal"

    def __init__(self, name, *args, **kwargs):
        self.config: dict = utils.get_config(name)

        self.start_urls = self.config["start_urls"]
        self.allowed_domains = self.config["allowed_domains"]

        self.rules: list[Rule] = []
        for kwargs in self.config["rules"]:
            # 先将 link_extractor 实例化再替换掉原来的
            kwargs.update({"link_extractor": LinkExtractor(**kwargs["link_extractor"])})
            self.rules.append(Rule(**kwargs))

        super(UniversalSpider, self).__init__(*args, **kwargs)

    def parse_detail(self, response: Response):
        item_conf: dict | None = self.config.get("item")
        loader_conf: dict | None = self.config.get("loader")
        if not item_conf or not loader_conf:
            self.logger.warning("未配置 item/loader 信息")
            return

        item = item_class_factory(item_conf["class"], item_conf["attrs"].keys())()
        loader_cls = loader_factory(loader_conf["class"], loader_conf["attrs"])
        loader = loader_cls(item, response=response)

        for key, extractor in item_conf["attrs"].items():
            loader_add = getattr(loader, f"add_{extractor['method']}")
            loader_add(key, extractor["arg"], re=extractor.get('re'))

        yield loader.load_item()
