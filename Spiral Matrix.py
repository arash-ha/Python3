"""
Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not len(matrix):
            return res
        n, m = len(matrix), len(matrix[0])
        up, down, left, right = 0, n - 1, 0, m - 1
        while len(res) < (n * m):
            for i in range(left, right + 1):
                if len(res) < (n * m):
                    res.append(matrix[up][i])

            for i in range(up + 1, down):
                if len(res) < (n * m):
                    res.append(matrix[i][right])

            for i in range(right, left - 1, -1):
                if len(res) < (n * m):
                    res.append(matrix[down][i])

            for i in range(down - 1, up, -1):
                if len(res) < (n * m):
                    res.append(matrix[i][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return res