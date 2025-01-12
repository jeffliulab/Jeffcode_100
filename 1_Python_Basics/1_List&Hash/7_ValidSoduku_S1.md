另一种解法见BitManipulation

不考虑是否能解，只考虑是否在row, col, sub-matrix上存在重复的solution：
```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows and columns
        for i in range(len(board)):
            row = set()
            col = set()
            for j in range(len(board[0])):
                if board[i][j] != '.' and board[i][j] in row:
                    return False
                row.add(board[i][j])

                if board[j][i] != '.' and board[j][i] in col:
                    return False
                col.add(board[j][i])
        
        # check sub matrix
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                nums = set()
                for k in range(3):
                    for l in range(3):
                        value = board[i + k][j + l]
                        if value != '.' and value in nums:
                            return False
                        nums.add(value)


        # overall result
        return True
```