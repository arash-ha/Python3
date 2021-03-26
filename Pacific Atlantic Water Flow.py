
"""
Pacific Atlantic Water Flow

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""

class Solution(object):
    def __init__(self):
        self.res = []  
        self.visited = []

    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return self.res
        m, n = len(matrix), len(matrix[0])
        self.visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            self.dfs(matrix, i, 0, float('-inf'), 1)
            self.dfs(matrix, i, n - 1, float('-inf'), 2)
        for j in range(n):
            self.dfs(matrix, 0, j, float('-inf'), 1)
            self.dfs(matrix, m - 1, j, float('-inf'), 2)
        return self.res

    def dfs(self, mat, x, y, preh, prev):
        if x < 0 or x >= len(mat) or y < 0 or y >= len(mat[0]) or mat[x][y] < preh or (self.visited[x][y]&prev) == prev:
            return
        self.visited[x][y] |= prev
        if (self.visited[x][y] == 3): self.res += [x, y],
        self.dfs(mat, x + 1, y, mat[x][y], self.visited[x][y]) 
        self.dfs(mat, x - 1, y, mat[x][y], self.visited[x][y])
        self.dfs(mat, x, y + 1, mat[x][y], self.visited[x][y])
        self.dfs(mat, x, y - 1, mat[x][y], self.visited[x][y])