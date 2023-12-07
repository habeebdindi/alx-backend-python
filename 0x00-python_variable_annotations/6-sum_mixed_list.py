#!/usr/bin/env python3
"""This module contains a function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function takes a list mxd_lst of integers and floats and
       returns their sum as a float.
    """
    return float(sum(mxd_lst))
