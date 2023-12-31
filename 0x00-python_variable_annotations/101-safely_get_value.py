#!/usr/bin/env python3
"""Annotatiing the function in this module
"""
from typing import Sequence, Union, Any, Mapping, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Safely gets value"""
    if key in dct:
        return dct[key]
    else:
        return default
