#!/usr/bin/env python3

"""
demo script of redis with python
"""


import redis
from typing import Any, Union, Optional, Callable
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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
            byte, int, float, None]:
        """method converts byte to original format using the key"""

        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """auto paramatises Caache.get with correct conversion function"""

        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """auto paramatises Caache.get with correct conversion function"""

        return self.get(key, int)
