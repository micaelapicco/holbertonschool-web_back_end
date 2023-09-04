#!/usr/bin/env python3
"""
Task 9:
return values with the appropriate types
"""
from typing import Tuple, Sequence, Iterable, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element lenght func"""
    return [(i, len(i)) for i in lst]
