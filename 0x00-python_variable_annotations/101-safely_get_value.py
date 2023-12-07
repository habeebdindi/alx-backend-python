#!/usr/bin/env python3
"""Annotatiing the function in this module
"""
from typing import Sequence, Union, Any

def safely_get_value(dct, key, default = None):
    """Safely gets value"""
    if key in dct:
        return dct[key]
    else:
        return default
