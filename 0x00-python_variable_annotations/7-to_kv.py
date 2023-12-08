#!/usr/bin/env python3
"""This module contains a function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function that takes a string k and an int OR float v as arguments.
       Returns a tuple.
    """
    return (k, v ** 2)
