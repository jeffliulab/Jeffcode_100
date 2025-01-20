question
```
Input: prices = [10,1,5,6,7,1]

Output: 6

Input: prices = [10,8,7,5,2]

Output: 0
```
solution
```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
```