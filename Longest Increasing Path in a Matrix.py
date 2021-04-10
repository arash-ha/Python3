"""
Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed). 

Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:

Input: matrix = [[1]]
Output: 1

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 2^31 - 1
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            dirs = {(i-1,j), (i+1,j), (i,j-1), (i,j+1)}
            for x, y in dirs:
                if 0 <= x < n and 0 <= y < m:
                    if matrix[x][y] > matrix[i][j]:
                        dp[i][j] = max(dp[i][j], dfs(x, y))
            dp[i][j] += 1
            return dp[i][j]

        if not matrix or not matrix[0]:
            return 0
        res = 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                res = max(res, dfs(i, j))
        return res

