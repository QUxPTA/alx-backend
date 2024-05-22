#!/usr/bin/env python3
"""
A class MRUCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache inherits from BaseCaching and
    is a caching system with MRU eviction policy
    """

    def __init__(self):
        """ Initialize the class with parent class properties """
        super().__init__()
        self.order = []  # To keep track of the usage order

    def put(self, key, item):
        """ Add an item in the cache using MRU policy """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the most recently used item
                mru_key = self.order.pop()
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None


if __name__ == "__main__":
    mru_cache = MRUCache()
