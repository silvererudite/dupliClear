class Hashmap:
    def __init__(self, size) -> None:
        self.size = size
        self.map = [[] for _ in range(self.size)]

    def _hash(self, key):
        hash_val = 0
        for char in str(key):
            hash_val += ord(char)

        return hash_val % self.size

    def add(self, key, value):
        index = self._hash(key)
        for entry in self.map[index]:
            if entry[0] == key:
                entry[1] = value
                return
        self.map[index].append([key, value])

    def get(self, key):
        idx = self._hash(key)
        for item in self.map[idx]:
            if item[0] == key:
                return item[1]
        raise KeyError(f"key {key} not found in hash map")
    
    def remove(self, key):
        idx = self._hash(key)
        for i, item in enumerate(self.map[idx]):
            if item[0] == key:
                del self.map[idx][i]
                return
        raise KeyError(f"key {key} not found in hash map")
        
