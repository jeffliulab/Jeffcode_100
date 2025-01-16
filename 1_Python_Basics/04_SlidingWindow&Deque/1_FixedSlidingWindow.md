找出一个字符串中所有长度为k的子串中，包含不同字符数最多的子串。

```py
# "找出一个字符串中所有长度为k的子串中，包含不同字符数最多的子串"
def maxUnique(s: str, k: int) -> int:
    if not s or k > len(s):
        return 0
    
    window = {}  # 用字典记录窗口中每个字符的频率
    max_count = 0
    
    # 初始化第一个窗口（处理前k个字符）
    for i in range(k):
        window[s[i]] = window.get(s[i], 0) + 1
    max_count = len(window)  # 不同字符的数量就是字典的长度
    
    # 滑动窗口处理剩余字符
    for i in range(k, len(s)):
        # 移除窗口最左边的字符
        window[s[i-k]] -= 1
        if window[s[i-k]] == 0:  # 如果字符频率为0，从字典中删除
            del window[s[i-k]]
            
        # 添加新字符到窗口
        window[s[i]] = window.get(s[i], 0) + 1
        
        # 更新最大不同字符数
        max_count = max(max_count, len(window))
    
    return max_count

if __name__ == "__main__":
    s = "abccccdefgggggkkk"
    print(maxUnique(s,5))
```