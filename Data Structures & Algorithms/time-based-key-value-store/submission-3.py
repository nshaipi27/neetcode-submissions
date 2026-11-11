class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        entries = self.time_map[key]
        l = 0
        r = len(entries) - 1
        result = ''
        while l <= r:
            m = (l + r) //2
            if entries[m][1] > timestamp:
                r = m - 1
            else:
                result = entries[m][0]
                l = m + 1
        return result
