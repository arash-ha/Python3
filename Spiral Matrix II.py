"""
Spiral Matrix II


Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0]*n for _ in range(n)]
        if n <= 0:
            return result
        up, down, left, right, num = 0, n - 1, 0, n - 1, 1
        while up <= down and left <= right:

            for i in range(left, right+1):
                result[up][i] = num
                num += 1

            for i in range(up+1, down+1):
                result[i][right] = num
                num += 1

            for i in range(right-1, left-1, -1):
                result[down][i] = num
                num += 1

            for i in range(down-1, up, -1):
                result[i][left] = num
                num += 1

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result