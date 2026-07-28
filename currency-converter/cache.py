import time

class Cache:
    def __init__(self, ttl_seconds=3600):
        self._data = {}
        self._times = {}

    def get(self, key):
        if key in self._data:
            age = time.time() - self._times[key]
            if age < self._ttl_seconds:
                return self._data[key]
            else:
                del self._data[key]
                del self._times[key]
        return None

    def set(self, key, value):
        self._data[key] = value
        self._times[key] = time.time()
        
