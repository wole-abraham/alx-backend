#!/usr/bin/env python3
"""
Write a function named index_range
that takes two integer arguments pag
e and page_size.

The function should return a tuple of
size two containing a start index and
an end index corresponding to the range
of indexes to return in a list for those
particular pagination parameters.
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """returns a tuple of size two containing
        a start index and an end undex correspoding
        o the range of indexs"""
        page_index = (page * page_size) - page_size
        page_limit = page_index + page_size
        return (page_index, page_limit)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get page retruns  """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        pag = self.index_range(page, page_size)
        data = self.dataset()[pag[0]: pag[1]]
        return data
