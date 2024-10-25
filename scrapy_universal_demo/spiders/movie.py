from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Response


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
        print(response.url)
