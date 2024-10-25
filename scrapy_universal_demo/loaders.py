from itemloaders.processors import Identity, TakeFirst, Compose  # noqa
from scrapy.loader import ItemLoader


class MovieItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    categories_out = Identity()
    score_out = Compose(TakeFirst(), str.strip)
    drama_out = Compose(TakeFirst(), str.strip)
