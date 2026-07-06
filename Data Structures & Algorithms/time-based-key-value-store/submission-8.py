class TimeMap:

    def __init__(self):
        self.record = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.record[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.record: return ""
        pairs = self.record[key]
        l, r = 0, len(pairs) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if pairs[m][0] <= timestamp:
                res = pairs[m][1]
                l = m + 1
            else:
                r = m - 1
        return res