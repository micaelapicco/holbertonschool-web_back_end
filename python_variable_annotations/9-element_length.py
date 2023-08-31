#!/usr/bin/env python3
"""
Task 9:
return values with the appropriate types
"""
from typing import Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> Tuple[Sequence, int]:
    """return a tuples"""
    return [(i, len(i)) for i in lst]
