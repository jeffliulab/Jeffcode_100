```
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
```

Solution Ot(n)
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(':')', '[':']','{':'}'}
        for char in s:
            if char in mapping:
                stack.append(char)
            if char in mapping.values():
                if not stack:
                    return False
                check_char = stack.pop()
                if char != mapping[check_char]:
                    return False
        if not stack:
            return True
        else:
            return False
```

Brute Force Solution Ot(n^2)
```python
class Solution:
    def isValid(self, s: str) -> bool:
        filtered_s = ''.join(c for c in s if c in '()[]{}')        # 只保留括号
        
        while '()' in filtered_s or '{}' in filtered_s or '[]' in filtered_s: # 不断移除匹配的括号对
            filtered_s = filtered_s.replace('()', '')
            filtered_s = filtered_s.replace('{}', '')
            filtered_s = filtered_s.replace('[]', '')
        
        return filtered_s == '' # 如果最终为空字符串，则括号完全匹配

```