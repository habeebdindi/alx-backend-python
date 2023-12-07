#!/usr/bin/env python3
"""Annotatiing the function in this module
"""
from typing import Iterable, Sequence, List, Tuple, Union


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes in an iterable and returns a list of tuples"""
    return [(i, len(i)) for i in lst]
