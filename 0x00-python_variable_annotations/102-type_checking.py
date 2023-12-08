#!/usr/bin/env python3
"""Correcting this module to be in line with mypy
"""

from typing import Tuple, Any, List, Union


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = tuple([
        item for item in lst
        for i in range(int(factor))
    ])
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
