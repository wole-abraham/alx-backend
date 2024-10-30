#!/usr/bin/env python3
""" FiFo caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Fifo caching"""
    def __init__(self):
        """ initializes init from super class  """
        super().__init__()

    def put(self, key, item):
        """ assignd the key to the value """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]

    def get(self, key):
        """ return value of the key if exists  """
        return self.cache_data.ge(key)
