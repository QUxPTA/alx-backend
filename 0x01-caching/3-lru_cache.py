#!/usr/bin/env python3
"""
A class LRUCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache inherits from BaseCaching and
    is a caching system with LRU eviction policy
    """

    def __init__(self):
        """ Initialize the class with parent class properties """
        super().__init__()
        self.order = []  # To keep track of the usage order

    def put(self, key, item):
        """ Add an item in the cache using LRU policy """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the least recently used item
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None


if __name__ == "__main__":
    lru_cache = LRUCache()
