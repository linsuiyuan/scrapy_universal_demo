"""
导入 itemloaders.processors 里定义的类型
同时定义一些自定义的 Item Processors
"""
from itemloaders.processors import (TakeFirst,  # noqa
                                    Identity,
                                    Join,
                                    SelectJmes,
                                    Compose,
                                    MapCompose)


class Strip:
    """
    去除首尾空格，是对 str.strip 的包装
    """

    def __call__(self, value: str) -> str:
        return value.strip()


