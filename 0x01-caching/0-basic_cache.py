#!/usr/bin/env python3
""" basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCaceh inherited """

    def __init__(self):
        """ initializes the class using the super class"""
        super().__init__()

    def put(self, key, item):
        """
            assigns the key and value to
            self.cache_data
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """retrieve the value of the key if exists """
        item = self.cache_data.get(key)
        return item
