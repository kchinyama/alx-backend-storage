#!/usr/bin/env python3

"""
demo script of redis with python
"""


import redis
from typing import Any, Union
import uuid


class Cache():
    """class that holds a cache object in a redis database"""

    def __init__(self):
        """constructor of the redis objects"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates random key, stores the data and returns the key"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
