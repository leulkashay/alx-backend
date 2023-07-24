#!/usr/bin/env python3
"""
Pagination
"""
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    a function named index_range that
    takes two integer argument page
    and page_sizr and return atuple
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)



class Server:
    """
    Server class to paginate adataset popular by baby names.
    """
    file_data = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self._dataset is None:
            with open(self.file_data) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int=1, page_size: int=10) -> List[List]:
        """
        paginate the dataset
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        paginate_range = index_range(page, page_size)
        start, end = paginate_range[0], paginate_range[1]
        dataset = self.dataset()

        try:
            data = [dataset[i] for i in range(start, end)]
        except IndexError:
            data = []

        return data
