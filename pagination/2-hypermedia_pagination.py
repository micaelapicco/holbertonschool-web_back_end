#!/usr/bin/env python3
"""
Task 2:
Implement a get_hyper
"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start
    index and an end index"""
    start_index = int(page * page_size - page_size)
    end_index = int(start_index + page_size)
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        pages = index_range(page=page, page_size=page_size)
        data = self.dataset()
        return data[pages[0]:pages[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """get hypermedia"""
        data = self.get_page(page, page_size)
        dataset = len(self.dataset())
        total_pages = int(dataset / page_size)
        next_page = 0
        prev_page = 0

        if next_page + 1 <= total_pages:
            next_page = page + 1
        else:
            next_page = None

        if prev_page - 1 >= 1:
            prev_page = page - 1
        else:
            prev_page = None

        dict_values = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return dict_values
