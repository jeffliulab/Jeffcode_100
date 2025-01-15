Longest Substring Without Repeating Characters

L1: Find the length of longest substring

L2: Find the substring

```
Input: s = "zxyzxyz"

Output_L1: 3
Output_L2: "zxy,xyz,yzx"

Input: s = "xxxx"

Output_L1: 1
Output_L2: "x"
```

## L1 Solution

Solution Ot(n)
```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if  len(s) == 1:
            return 1
        output = 0
        l = 0
        r = 0
        window = set()
        while(r<len(s)):
            while(s[r] in window):
                window.remove(s[l])
                l += 1
            window.add(s[r])
            output = max(output, len(window))
            r += 1
        return output
```

optimize one (same Ot)
与前面的版本相比，这个版本使用了哈希表（mp）来记录字符的最新位置，从而进一步提高了性能和逻辑清晰度。
```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
```

## L2 Find the substring