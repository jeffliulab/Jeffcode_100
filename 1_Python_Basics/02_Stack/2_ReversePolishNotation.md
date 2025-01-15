```
Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

Example:
Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5

```

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ['+', '-', '*', '/']
        for element in tokens:
            if element not in operator:
                stack.append(element)
            else:
                ope = element
                num2 = stack.pop()
                num1 = stack.pop()
                if ope == '+':
                    stack.append(int(num1)+int(num2))
                elif ope == '*':
                    stack.append(int(num1)*int(num2))
                elif ope == '-':
                    stack.append(int(num1)-int(num2))
                elif ope== '/':
                    stack.append(int(float(num1)/float(num2)))
        return int(stack[0])
```

