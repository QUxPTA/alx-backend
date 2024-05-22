#!/usr/bin/env python3
"""
A class LFUCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching and
    is a caching system with LFU eviction policy
    """

    def __init__(self):
        """ Initialize the class with parent class properties """
        super().__init__()
        # To keep track of the usage frequency of each key
        self.usage_frequency = {}
        self.order = []  # To keep track of the usage order of keys

    def put(self, key, item):
        """ Add an item in the cache using LFU policy """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.usage_frequency[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Find the least frequently used key(s)
                    min_freq = min(self.usage_frequency.values())
                    least_used_keys = [
                        k for k, v in self.usage_frequency.items()
                        if v == min_freq]

                    # If there is more than one key with
                    # the same minimum frequency, use LRU to discard
                    if len(least_used_keys) > 1:
                        for k in self.order:
                            if k in least_used_keys:
                                discard_key = k
                                break
                    else:
                        discard_key = least_used_keys[0]

                    del self.cache_data[discard_key]
                    del self.usage_frequency[discard_key]
                    self.order.remove(discard_key)
                    print("DISCARD:", discard_key)

                self.cache_data[key] = item
                self.usage_frequency[key] = 1

            # Update the usage order
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.usage_frequency[key] += 1
            # Update the usage order
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None


if __name__ == "__main__":
    lfu_cache = LFUCache()
