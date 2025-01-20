下面的几种方法Efficiency是一样

```python
class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        ls = self.data[key]

        l = 0
        r = len(ls) - 1
        while(l <= r):
            mid = (l+r)//2
            if ls[mid][0] == timestamp:
                return ls[mid][1]
            elif ls[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        # 这里是本题的最关键的地方
        # 当二分查找结束后，如果没有找到，且r < 0
        # 说明没有任何时间戳小于或等于 timestamp，需要返回空字符串 ""
        if r < 0:
            return ""
        # 如果r>=0，说明没有该时间戳，但是有符合最新要求的时间戳
        else:
            return ls[r][1]
```

可以优化一下：
```python
class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
```

使用SortedDict：
```python
from sortedcontainers import SortedDict

class TimeMap:
    def __init__(self):
        self.m = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        
        timestamps = self.m[key]
        idx = timestamps.bisect_right(timestamp) - 1
        
        if idx >= 0:
            closest_time = timestamps.iloc[idx]
            return timestamps[closest_time]
        return ""
```