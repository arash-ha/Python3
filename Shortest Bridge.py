"""
Shortest Bridge

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
You may change 0's to 1's to connect the two islands to form one island.
Return the smallest number of 0's you must flip to connect the two islands.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 
Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or (i, j) in seen or grid[i][j] != 1:
                return
            seen.add((i, j))
            q.append((i, j, 0))
            grid[i][j] = -1
            list(map(dfs, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))

        seen, q, m, n = set(), deque(), len(grid), len(grid[0])
        for i, j in product(range(m), range(n)):
            if grid[i][j]:
                dfs(i, j)
                break

        while q:
            i, j, h = q.popleft()
            if grid[i][j] == 1:
                return h - 1
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                    seen.add((x, y))
                    q += (x, y, h + 1),
        return -1