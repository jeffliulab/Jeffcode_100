在之前几道的基础上，这道换汤不换药，不过唯一要注意的就是比较两个dict的时候，如果清空的key没有del，可能会导致dict1==dict2的结果不准确。

Solution Ot(n):
```py
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # initialize
        word = s1
        s = s2
        if len(word) > len(s):
            return False
        dt = {}
        for c in word:
            dt[c] = dt.get(c, 0) + 1
        
        # initialize sliding window
        l = 0
        window = {}
        r = 0
        for r in range(len(word)):
            window[s[r]] = window.get(s[r], 0) + 1
        if dt == window:
            return True

        # sliding
        for r in range(r+1,len(s)):
            # r slide to right
            window[s[r]] = window.get(s[r], 0) + 1
            # l slide to right
            window[s[l]] -= 1
            if window[s[l]] == 0:
                del window[s[l]]
            l += 1
            if dt == window:
                return True
        
        return False
```

我的解法（上面这个）虽然简洁且Os(1)，但是dt==window这个开销比较大，可以参考一下neetcode的解法，虽然整体Ot和Os是一样的，但是空间开销稍微少一点：
```py
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
```
