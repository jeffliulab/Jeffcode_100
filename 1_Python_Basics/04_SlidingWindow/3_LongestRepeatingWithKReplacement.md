Longest Repeating Character with K Replacement

Question
```
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Input: s = "XYYX", k = 2

Output: 4

Input: s = "AAABABB", k = 1

Output: 5
```

Solution Ot(n)
```py
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = {}
        maxc = 0
        l = 0
        output = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            maxc = max(maxc, window[s[r]])
            window_size = r - l + 1
            need_change = window_size - maxc
            while(need_change > k):
                window[s[l]] -= 1
                l += 1
                # maxc = max(maxc, window[s[r]]) 这里不需要重新计算
                # 保持一个较大的maxc，可以让效率更高
                window_size = r - l + 1
                need_change = window_size - maxc
            output = max(output, window_size)
        return output
```