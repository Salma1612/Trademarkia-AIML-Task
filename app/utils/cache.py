
class SemanticCache:
    def __init__(self):
        self.store = {}
        self.hit_count = 0
        self.miss_count = 0

    def get(self, key):
        if key in self.store:
            self.hit_count += 1
            return self.store[key], True
        self.miss_count += 1
        return None, False

    def set(self, key, value):
        self.store[key] = value

    def clear(self):
        self.store = {}
        self.hit_count = 0
        self.miss_count = 0

    def stats(self):
        total = len(self.store)
        hit_rate = self.hit_count / (self.hit_count + self.miss_count) if (self.hit_count + self.miss_count) > 0 else 0
        return {
            "total_entries": total,
            "hit_count": self.hit_count,
            "miss_count": self.miss_count,
            "hit_rate": round(hit_rate, 3)
        }
