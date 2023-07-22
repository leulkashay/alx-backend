#!/usr/bin/env python3
"""
Pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    a function named index_range that
    takes two integer argument page
    and page_sizr and return atuple
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
