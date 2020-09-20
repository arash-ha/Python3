"""
Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if n == 0 or m == 0: return 0
        paths = [[0]*m for i in range(n)]

        init = 1
        for c in range(m-1, -1, -1):
            if obstacleGrid[n-1][c] == 1: init = 0
            paths[n-1][c] = init

        init = 1;
        for r in range(n-1, -1, -1):
            if obstacleGrid[r][m-1] == 1: init = 0
            paths[r][m-1] = init

        for r in range(n-2, -1, -1):
            for c in range(m-2, -1, -1):
                if obstacleGrid[r][c] == 0:
                    paths[r][c] = paths[r][c+1] + paths[r+1][c]

        return paths[0][0]