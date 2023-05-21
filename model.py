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
    
    def __iter__(self):
        self.current_bucket = 0
        self.current_entry = 0
        return self

    def __next__(self):
        while self.current_bucket < self.size:
            if self.current_entry < len(self.map[self.current_bucket]):
                entry = self.map[self.current_bucket][self.current_entry]
                self.current_entry += 1
                return entry
            else:
                self.current_bucket += 1
                self.current_entry = 0
        raise StopIteration
    
    def __contains__(self, key):
        index = self._hash(key)
        for entry in self.map[index]:
            if entry[0] == key:
                return True
        return False

# hash_map = Hashmap(10)
# hash_map.add("A", 19)
# hash_map.add("B", 12)
# hash_map.add("C", 96)

# for key, value in hash_map:
#     print(f"Key: {key}, Value: {value}")

# print("A" in hash_map)  # Output: True
# print("AC" in hash_map)  # Output: False