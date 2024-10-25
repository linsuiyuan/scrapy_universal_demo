from itemloaders.processors import TakeFirst, Identity, Compose  # noqa
from scrapy import Field, Item


class MovieItem(Item):
    name = Field()
    cover = Field()
    categories = Field()
    published_at = Field()
    drama = Field()
    score = Field()
