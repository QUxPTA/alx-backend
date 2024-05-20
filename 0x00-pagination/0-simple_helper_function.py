#!/usr/bin/env python3
"""
A fuunction that returns a tuple of size two
containing a start index and an end index
"""


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
