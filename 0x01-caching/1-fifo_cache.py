#!/usr/bin/env python3
"""
FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    a class that inherits from
    base caching and is a caching system
    """
    def __init__(self):
        """
        initialize the cache
        """
        super().__init__()
        self.cache_data_list =[]

    def put(self, key, item):
        """
        assign the given key to the given item
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data_list.append(key)
            if len(self.cache_data_list) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.cache_data_list[0])
                discard = self.cache_data_list.pop(0)
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """
        get the key from 5he cache
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            pass
