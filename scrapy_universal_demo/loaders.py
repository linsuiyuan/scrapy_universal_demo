from itemloaders import processors  # noqa
from itemloaders.processors import Identity, TakeFirst, Compose  # noqa
from scrapy.loader import ItemLoader


class MovieItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    categories_out = Identity()
    score_out = Compose(TakeFirst(), str.strip)
    drama_out = Compose(TakeFirst(), str.strip)


def processor_fatory(processor: str, *arg: str):

    match processor:
        case x if x in ("Identity", "TakeFirst"):
            return getattr(processors, processor)()

        case "Join":
            if not arg:
                return getattr(processors, processor)()
            else:
                return getattr(processors, processor)(*arg)

        case "SelectJmes":
            # todo 待测试
            return getattr(processors, processor)(*arg)

        case x if x in ("Compose", "MapCompose"):
            # 递归组合后返回
            compose = getattr(processors, processor)
            return compose(*[processor_fatory(a) for a in arg])

        case _:
            # 内置的或者其他函数（str.strip, lambda 等）
            return eval(processor)


def loader_factory(loader_name, attrs):
    attr_dict = {}
    for key, value in attrs.items():
        if isinstance(value, str):
            attr_dict[key] = processor_fatory(value)
        elif isinstance(value, list):
            processor, arg = value
            attr_dict[key] = processor_fatory(processor, *arg)
        else:
            raise TypeError("loader配置的类型只能为字符串或列表")

    loader = type(loader_name,
                  (ItemLoader,),
                  attr_dict)
    return loader
