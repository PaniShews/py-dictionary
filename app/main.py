class Dictionary:
    def __init__(
            self,
            capacity: int = 8
    ) -> None:
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(
            self,
            key: int
    ) -> int:
        return hash(key) % self.capacity

    def __setitem__(
            self,
            key: int,
            value: any
    ) -> None:
        index = self._hash(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])
        self.size += 1

    def __getitem__(
            self,
            key: int
    ) -> tuple:
        index = self._hash(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        raise KeyError(f"Key '{key}' not found")

    def __len__(self) -> int:
        return self.size
