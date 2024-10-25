from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Response

from scrapy_universal_demo.items import MovieItem, MovieItemLoader


class MovieSpider(CrawlSpider):
    name = "movie"
    allowed_domains = ["ssr1.scrape.center"]
    start_urls = ["https://ssr1.scrape.center"]

    rules = (
        Rule(LinkExtractor(restrict_css=".item .name"),
             follow=True, callback="parse_detail"),
        Rule(LinkExtractor(restrict_css=".next"),
             follow=True),
    )

    def parse_detail(self, response: Response):
        item = MovieItem()
        loader = MovieItemLoader(item=item, response=response)
        loader.add_css("name", ".item h2::text")
        loader.add_css("cover", ".cover::attr(src)")
        loader.add_css("categories", ".categories .category span::text")
        loader.add_css("published_at", ".info span::text", re=r"(\d{4}-\d{2}-\d{2})\s?上映")
        loader.add_css("drama", ".drama p::text")
        loader.add_css("score", "p.score::text")
        yield loader.load_item()
