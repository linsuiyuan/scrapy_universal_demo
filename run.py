from argparse import ArgumentParser

from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

from scrapy_universal_demo import utils

parser = ArgumentParser(description="通用 Spider")
parser.add_argument("name", help="需要爬取的 Spider 的名称")
name: str = parser.parse_args().name


def run():
    try:
        config: dict = utils.get_config(name.lower())
    except FileNotFoundError:
        print(f"相应的配置文件【{name}】不存在")
        return

    spider = config.get("spider", "universal")
    settings = dict(get_project_settings())
    settings.update(config.get("settings"))

    process = CrawlerProcess(settings)
    process.crawl(spider, name=name)
    process.start()


if __name__ == "__main__":
    run()
