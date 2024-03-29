"""
Stone Game II

Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 
Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104
 
Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 10^4
"""
# Solution I
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= n: return piles[i]
            return piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        return dp(0, 1)
    
# Solution II

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def dfs(start, m):
            res = 0
            total = sum(piles[start:])
            for i in range(1, min(2 * m + 1, len(piles) - start + 1)):
                optima = dfs(start + i, max(m, i))
                res = max(res, total - optima)
            return res
        return dfs(0, 1)