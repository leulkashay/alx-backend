#!/usr/bin/env python3
"""
LRU caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Inherits from basecaching
    """
    def __init___(self):
        """
        initilaze LRU caching
        """
        super().__init__()
        self.queue = []

    def put(self, key,  item):
        """
        Assiging key and items
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.queue:
            discard = self.queue.pop(0)
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Fetch data with key
        """
        if not key or key not in self.cache_data:
            return None
        # Remove from any position in the queue and add to the back
        self.queue.remove(key)
        self.queue.append(key)

        return self.cache_data[key]
