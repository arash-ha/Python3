"""
Unique Binary Search Trees

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:

Input: n = 3
Output: 5

Example 2:

Input: n = 1
Output: 1
 
Constraints:

1 <= n <= 19
"""

# Solution I
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]
    
# Soution II
class Solution:
    def numTrees(self, n: int) -> int:
        def helper(low, high) -> int:
            if low >= high:
                return 1
            res = 0
            for i in range(low, high + 1):
                res += helper(low, i - 1) * helper(i + 1, high)
            return res
        
        return helper(1, n)