"""
Number of Closed Islands

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
Return the number of closed islands.

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 
Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <= 1
"""
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    if self.bfs(grid, i, j):
                        res += 1
        return res

    def bfs(self, grid, i, j):
        grid[i][j] = -1
        q = collections.deque()
        q.append([i, j])
        flag = True
        while q:
            x, y = q.popleft()
            if x == 0 or x >= len(grid) - 1 or y == 0 or y >= len(grid[0]) - 1:
                flag = False
            if x - 1 >= 0 and grid[x - 1][y] == 0:
                grid[x - 1][y] = -1
                q.append([x - 1, y])

            if x + 1 < len(grid) and grid[x + 1][y] == 0:
                grid[x + 1][y] = -1
                q.append([x + 1, y])

            if y - 1 >= 0 and grid[x][y - 1] == 0:
                grid[x][y - 1] = -1
                q.append([x, y - 1])

            if y + 1 < len(grid[0]) and grid[x][y + 1] == 0:
                grid[x][y + 1] = -1
                q.append([x, y + 1])
        return flag