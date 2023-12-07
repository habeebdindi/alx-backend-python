#!/usr/bin/env python3
"""This module contains a function that returns a float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """function  takes a list input_list of floats as argument and returns
    their sum as a float.
    """
    return float(sum(input_list))
