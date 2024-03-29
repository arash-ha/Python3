"""
Rotting Oranges

You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        r, c, fresh, t = len(grid), len(grid[0]), 0, 0
        for i in range(r):
            for j  in range(c):
                if grid[i][j] == 2:
                    rotten.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1

        while rotten:
            num = len(rotten)
            for i in range(num):
                x, y = rotten[0]
                rotten.pop(0)
                if x > 0 and grid[x - 1][y] == 1:
                    grid[x - 1][y] = 2
                    fresh -= 1
                    rotten.append([x - 1, y])

                if y > 0 and grid[x][y - 1] == 1:
                    grid[x][y - 1] = 2
                    fresh -= 1
                    rotten.append([x, y - 1])

                if x < r - 1 and grid[x + 1][y] == 1:
                    grid[x + 1][y] = 2
                    fresh -= 1
                    rotten.append([x + 1, y])

                if y < c - 1 and grid[x][y + 1] == 1:
                    grid[x][y + 1] = 2
                    fresh -= 1
                    rotten.append([x, y + 1])

            if rotten:
                t += 1

        return t if fresh == 0 else -1