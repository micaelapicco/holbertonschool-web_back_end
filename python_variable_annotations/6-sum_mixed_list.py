#!/usr/bin/env python3
"""
Task 6:
Write a type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns their sum as a float"""
    return sum(mxd_lst)
