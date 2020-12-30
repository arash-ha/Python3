"""
Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

Note:

The total number of elements of the given matrix will not exceed 10,000.
"""

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or not matrix:
            return []
        n, m = len(matrix), len(matrix[0])
        row, column = 0, 0
        direction, i = 1, 0
        res = []
        while row < n and column < m:
            res.append(matrix[row][column])
            i += 1
            new_row = row + (-1 if direction == 1 else 1)
            new_column = column + (1 if direction == 1 else -1)
            if new_row < 0 or new_row == n or new_column < 0 or new_column == m:
                if direction == 1:
                    row += (1 if column == m - 1 else 0)
                    column += (1 if column < m - 1 else 0)
                else:
                    column += (1 if row == n - 1 else 0)
                    row += (1 if row < n - 1 else 0)
                direction = 1 - direction
            else:
                row = new_row
                column = new_column
        return res