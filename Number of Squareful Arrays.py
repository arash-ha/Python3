"""
Number of Squareful Arrays

An array is squareful if the sum of every pair of adjacent elements is a perfect square.
Given an integer array nums, return the number of permutations of nums that are squareful.
Two permutations perm1 and perm2 are different if there is some index i such that perm1[i] != perm2[i].

Example 1:

Input: nums = [1,17,8]
Output: 2
Explanation: [1,8,17] and [17,8,1] are the valid permutations.

Example 2:

Input: nums = [2,2,2]
Output: 1
 
Constraints:

1 <= nums.length <= 12
0 <= nums[i] <= 10^9
"""

class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        res = []
        self.backtrack(sorted(A), [], res)
        return len(res)
    
    def backtrack(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if path and not self.isSquare(path[-1] + nums[i]):
                continue
            self.backtrack(nums[:i]+nums[i+1:], path+[nums[i]], res)
        
    def isSquare(self, n):
        return pow(int(sqrt(n)), 2) == n