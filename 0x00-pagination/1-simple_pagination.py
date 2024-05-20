#!/usr/bin/env python3
"""
A fuunction that returns a tuple of size two
containing a start index and an end index
"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Calculate the start and end indices for pagination.

    Args:
    - page: The current page number (integer).
    - page_size: The number of items per page (integer).

    Returns:
    - A tuple (start_index, end_index) where:
      - start_index: The index of the first item on the page.
      - end_index: The index one past the last item on the page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
