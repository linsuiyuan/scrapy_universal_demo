import importlib
from functools import partial
from typing import Any

from universal import processors
from universal.processors import TakeFirst, Identity, Compose
from scrapy.loader import ItemLoader


class MovieItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
    categories_out = Identity()
    score_out = Compose(TakeFirst(), str.strip)
    drama_out = Compose(TakeFirst(), str.strip)


def processor_fatory(proc_list: list[Any]):
    """
    Processor 工厂
    :param proc_list: Processor类型和参数列表
    :return:
    """

    # 第一个是类型，后续的是参数，因为参数有可能为空，所以这里不使用解包
    proc_name = proc_list[0]
    args = proc_list[1:]
    match proc_name:
        case x if x in ("Identity", "TakeFirst"):
            return getattr(processors, proc_name)()

        case "Join":
            if not args:
                return getattr(processors, proc_name)()
            else:
                return getattr(processors, proc_name)(*args)

        case "SelectJmes":
            return getattr(processors, proc_name)(*args)

        case x if x in ("Compose", "MapCompose"):
            # 使用递归进行组合
            compose = getattr(processors, proc_name)
            return compose(*(processor_fatory(a) for a in args))

        # 自定义的类型
        case "Strip":
            return getattr(processors, proc_name)()

        case _:
            raise TypeError(f"不支持的Processor：{proc_name}")


def loader_class_factory(cls_name, attrs):
    """
    ItemLoder 类工厂
    :param cls_name: 类名
    :param attrs: 属性序列
    :return:
    """
    attr_dict = {key: processor_fatory(value)
                 for key, value in attrs.items()
                 }

    return type(cls_name,
                (ItemLoader,),
                attr_dict)
