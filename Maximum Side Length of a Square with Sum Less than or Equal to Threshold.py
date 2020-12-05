"""
Maximum Side Length of a Square with Sum Less than or Equal to Threshold

Given a m x n matrix mat and an integer threshold. Return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.
 

Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
Example 3:

Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
Output: 3
Example 4:

Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
Output: 2
 

Constraints:

1 <= m, n <= 300
m == mat.length
n == mat[i].length
0 <= mat[i][j] <= 10000
0 <= threshold <= 10^5
"""
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n, sm = len(mat), len(mat[0]), 0
        l = min(m, n)
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(0, m):
            for j in range(0, n):
                dp[i+1][j+1] = mat[i][j] + dp[i+1][j] + dp[i][j+1] - dp[i][j]

        for k in range(l, 0, -1):
            for i in range(k, m+1):
                for j in range(k, n+1):
                    sm = dp[i][j] - dp[i-k][j] - dp[i][j-k] + dp[i-k][j-k]
                    if sm <= threshold:
                        return k

        return 0