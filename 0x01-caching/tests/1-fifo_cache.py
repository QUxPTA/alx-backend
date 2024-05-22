#!/usr/bin/env python3
"""
A class FIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and
    is a caching system with FIFO eviction policy
    """

    def __init__(self):
        """ Initialize the class with parent class properties """
        super().__init__()
        self.order = []  # To keep track of the insertion order

    def put(self, key, item):
        """ Add an item in the cache using FIFO policy """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)  # Remove the oldest item
                del self.cache_data[oldest_key]
                print("DISCARD:", oldest_key)

    def get(self, key):
        """ Get an item by key """
        if key is not None:
            return self.cache_data.get(key)
        return None


if __name__ == "__main__":
    fifo_cache = FIFOCache()
