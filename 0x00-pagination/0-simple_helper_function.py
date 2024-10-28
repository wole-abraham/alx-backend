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


def index_range(page: int, page_size: int) -> tuple:
    """returns a tuple of size two containing
    a start index and an end undex correspoding
    to the range of indexs"""

    page_index = (page * page_size) - page_size
    page_limit = page_index + page_size
    return (page_index, page_limit)
