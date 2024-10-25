from itemloaders.processors import TakeFirst, Identity, Compose  # noqa
from scrapy import Field, Item
from scrapy.loader import ItemLoader


class MovieItem(Item):
    name = Field()
    cover = Field()
    categories = Field()
    published_at = Field()
    drama = Field()
    score = Field()


class MovieItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    categories_out = Identity()
    score_out = Compose(TakeFirst(), str.strip)
    drama_out = Compose(TakeFirst(), str.strip)
