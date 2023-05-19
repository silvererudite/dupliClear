class Hashmap:
    def __init__(self, size) -> None:
        self.size = size
        self.map = [[] for _ in range(self.size)]
    