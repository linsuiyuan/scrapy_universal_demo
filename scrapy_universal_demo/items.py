from typing import Iterable

from itemloaders.processors import TakeFirst, Identity, Compose  # noqa
from scrapy import Field, Item


class MovieItem(Item):
    name = Field()
    cover = Field()
    categories = Field()
    published_at = Field()
    drama = Field()
    score = Field()


def item_class_factory(item_name: str, attrs: Iterable[str]):
    return type(item_name,
                (Item,),
                {n: Field() for n in attrs})


if __name__ == '__main__':
    cls = item_class_factory("MovieItem", ("name", "score"))
    item = cls()
    item["name"] = "love"
    item["score"] = 9
    print(dict(item))
