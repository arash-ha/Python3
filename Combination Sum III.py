"""
Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(path, n, idx):
            if k == len(path):
                if n == 0: res.append(path.copy())
                return

            for i in range(idx, 10):
                if i > n: return;
                path.append(i)
                dfs(path, n-i, i+1)
                path.pop()
        dfs([], n , 1)
        return res
