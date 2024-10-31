#!/usr/bin/env python
""" LIFO caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Lifo Cache"""
    def __init__(self):
        """ initialize basecaching"""
        super().__init__()

    def put(self, key, item):
        """ adds to key in cache_data  """
        if key is None or item is None:
            pass
        else:
            if self.cache_data.get(key) is not None:
                del self.cache_data[key]
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_item = [x for x in self.cache_data.keys()][-2]
                print(f"DISCARD: {last_item}")
                del self.cache_data[last_item]

    def get(self, key):
        """ get value of key if exist """
        self.cache_data.get(key)
