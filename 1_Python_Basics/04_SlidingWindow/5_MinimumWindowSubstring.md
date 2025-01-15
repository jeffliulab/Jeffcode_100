Minimum Window Substring

这道题在不考虑t包含重复字母的情况下，初步解答如下：
```py
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        word = {}
        for char in t:
            word[char] = word.get(char, 0) + 1

        valid_count = 0
        
        # set window
        window = {}
        l = 0
        min_len = float('inf')
        min_len_start = l

        # sliding
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in word:
                valid_count += 1
            while valid_count == len(t):
                # find a valid solution
                # remember position
                if r - l + 1 < min_len:
                    min_len_start = l
                    min_len = r - l + 1

                # start sliding l
                if s[l] in word:
                    valid_count -= 1
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

        return "" if min_len == float('inf') else s[min_len_start:min_len_start+min_len] 
```

在此基础上，只需要把valid_count改成一个dict，然后将valid_count==len(t)这个条件改为word中的所有元素都包含在valid_count中：
Solution Ot(n*m), Os(m)
```py
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        word = {}
        for char in t:
            word[char] = word.get(char, 0) + 1

        valid_count = {}
        
        # set window
        window = {}
        l = 0
        min_len = float('inf')
        min_len_start = l

        # sliding
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in word:
                valid_count[s[r]] = valid_count.get(s[r], 0) + 1
            
            # while word elements all contains in valid_count dict
            while all(char in valid_count and valid_count[char] >= count for char, count in word.items()):
                # find a valid solution
                # remember position
                if r - l + 1 < min_len:
                    min_len_start = l
                    min_len = r - l + 1

                # start sliding l
                if s[l] in word:
                    valid_count[s[l]] -= 1
                    if valid_count[s[l]] == 0:
                        del valid_count[s[l]]
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

        return "" if min_len == float('inf') else s[min_len_start:min_len_start+min_len] 
```

进一步优化，使用have和need巧妙判断是否满足要求：
```py
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        word = {}
        for char in t:
            word[char] = word.get(char, 0) + 1

        valid_count = {}

        have, need = 0, len(word)  # optimize time efficiency
        
        # set window
        window = {}
        l = 0
        min_len = float('inf')
        min_len_start = l

        # sliding
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in word:
                valid_count[s[r]] = valid_count.get(s[r], 0) + 1
                ### 这里需要update
                # 当某个字符的数量恰好达到要求时
                if valid_count[s[r]] == word[s[r]]:  
                    have += 1
                
            
            while have >= need:
                # find a valid solution
                # remember position
                if r - l + 1 < min_len:
                    min_len_start = l
                    min_len = r - l + 1

                # start sliding l
                if s[l] in word:
                    valid_count[s[l]] -= 1
                    ### 这里需要update
                    # 当某个字符的数量小于要求时
                    if valid_count[s[l]] < word[s[l]]:   
                        have -= 1
                    if valid_count[s[l]] == 0:
                        del valid_count[s[l]]

                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

        return "" if min_len == float('inf') else s[min_len_start:min_len_start+min_len] 
```

neetcode上的参考：
```py
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                    
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
```