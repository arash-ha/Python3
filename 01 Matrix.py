"""
01 Matrix

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 
Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else 1e5
                    left = mat[r][c - 1] if c > 0 else 1e5
                    mat[r][c] = min(top, left) + 1

        for r in range(m-1, -1, -1):
            for c in range(n -1 , -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else 1e5
                    right = mat[r][c + 1] if c < n - 1 else 1e5
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat