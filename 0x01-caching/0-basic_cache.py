#!/usr/bin/env python3
"""
basic caching class
"""
from base_caching import BaseCaching


class base_caching(BaseCaching):
    """
    inherits from base_caching system
    """
    def __init__(self):
        """
        initalize the class
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        assigns the given key to the given item
        """
        if key and item:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """
        return the value of a given key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
