class MyHashMap:

    BUCKETS = 389
    def __init__(self):
        self.mem = [[] for _ in range(BUCKETS)]

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        self.mem[key % BUCKETS].append((key, value))

    def get(self, key: int) -> int:
        return next((v for k, v in self.mem[key % BUCKETS] if k == key), -1)
        
    def remove(self, key: int) -> None:
        xs = self.mem[key % BUCKETS]
        for k, v in xs:
            if k == key:
                xs.remove((k, v))
# Runtime: 228 ms, faster than 92.47% of Python3 online submissions for Design HashMap.
# Memory Usage: 17.1 MB, less than 96.99% of Python3 online submissions for Design HashMap.
