#!/usr/bin/env python3
"""
Task 0:
return a tuple of size two containing a start index and an
end index corresponding to the range of indexes to return in
a list for those particular pagination parameters.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start
    index and an end index"""
    start_index = int(page * page_size - page_size)
    end_index = int(start_index + page_size)
    return (start_index, end_index)
