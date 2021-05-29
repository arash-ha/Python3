"""
N-Queens II

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:

Input: n = 1
Output: 1
 
Constraints:

1 <= n <= 9
"""

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        def dfs(dep, r, d1, d2):
            if dep == n:
                self.res += 1
                return

            for i in range(n):
                cur = 1 << i
                if (cur & r) or (cur & d1) or (cur & d2):
                    continue
                dfs(dep + 1, (cur | r), (cur | d1) << 1, (cur | d2) >> 1)

        dfs(0, 0, 0, 0)
        return self.res