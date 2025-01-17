通过转换可以把2D视为1D去找

降维：
* index = x * col_count + y

升维：    
* x = index // col_count
* y = index % col_count

```py
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        COL = len(matrix[0]) # column length of matrix
        
        l = 0
        r = len(matrix) * COL - 1

        while(l<=r):
            mid_index = (l + r) // 2
            x = mid_index // COL
            y = mid_index % COL
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                r = mid_index - 1
            else:
                l = mid_index + 1
        
        return False
```