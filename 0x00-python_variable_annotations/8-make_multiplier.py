#!/usr/bin/env python3
"""THis module conatins a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function akes a float multiplier as argument and returns a
       function that multiplies a float by multiplier.
    """
    def multiplier_function(number: float) -> float:
        """function that multiplies a float by multiplier."""
        return float(number * multiplier)

    return multiplier_function
