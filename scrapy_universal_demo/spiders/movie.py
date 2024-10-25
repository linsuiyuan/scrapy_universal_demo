import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MovieSpider(CrawlSpider):
    name = "movie"
    allowed_domains = ["ssr1.scrape.center"]
    start_urls = ["https://ssr1.scrape.center"]

    rules = (Rule(LinkExtractor(allow=r"Items/"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        item = {}
        # item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # item["name"] = response.xpath('//div[@id="name"]').get()
        # item["description"] = response.xpath('//div[@id="description"]').get()
        return item
