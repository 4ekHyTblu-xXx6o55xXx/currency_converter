import time

class Cache:
    def __init__(self, ttl_seconds=3600):
        self._data = {}
        self._timestamps = {}
        self._ttl = ttl_seconds

    def get(self, key):
        if key in self._data:
            age = time.time() - self._timestamps[key]
            if age < self._ttl:
                return self._data[key]
            else:
                del self._data[key]
                del self._timestamps[key]
        return None

    def set(self, key, value):
        self._data[key] = value
        self._timestamps[key] = time.time()
