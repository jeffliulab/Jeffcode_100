## Simple Anagram

Input: s = "racecar", t = "carrace"

Output: true

Input: s = "jar", t = "jam"

Output: false

Solution:
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        return s_dict == t_dict
```

## Group Anagram

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Input: strs = ["x"]

Output: [["x"]]

Input: strs = [""]

Output: [[""]]

SOlution: O(n)
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_word = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in dict_word:
                dict_word[key] = []
            dict_word[key].append(word)

        return list(dict_word.values())
```

Solution: O(n^2)
```python
class Solution:
    def isAnagram(self, str1, str2):
        dict_1 = {}
        dict_2 = {}
        for char in str1:
            dict_1[char] = dict_1.get(char, 0) + 1
        for char in str2:
            dict_2[char] = dict_2.get(char, 0) + 1
        return dict_1 == dict_2

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        visited = set()

        # traverse strs
        for i in range(len(strs)):
            if i in visited:
                continue

            # if the element has an anagram in the list strs
            sub_list = []
            for j in range(i+1, len(strs)):
                if j in visited:
                    continue
                if self.isAnagram(strs[i], strs[j]):
                    sub_list.append(strs[j])
                    visited.add(j)
            sub_list.append(strs[i])
            visited.add(i)
            output.append(sub_list)
        return output
```