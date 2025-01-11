## Encoding and Decoding

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"#{s.replace('#','!!&&PLACEHOLDER&&!!')}" for s in strs)

    def decode(self, s: str) -> List[str]:
        list_string = s.split('#')
        list_string = [s.replace('!!&&PLACEHOLDER&&!!','#') for s in list_string]
        return list_string[1:]
```