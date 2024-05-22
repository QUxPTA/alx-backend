#!/usr/bin/env python3
"""
A class LIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and
    is a caching system with LIFO eviction policy
    """

    def __init__(self):
        """ Initialize the class with parent class properties """
        super().__init__()
        self.order = []  # To keep track of the insertion order

    def put(self, key, item):
        """ Add an item in the cache using LIFO policy """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the second last item, as the last item is newly added
                last_key = self.order.pop(-2)
                del self.cache_data[last_key]
                print("DISCARD:", last_key)

    def get(self, key):
        """ Get an item by key """
        if key is not None:
            return self.cache_data.get(key)
        return None


if __name__ == "__main__":
    lifo_cache = LIFOCache()
