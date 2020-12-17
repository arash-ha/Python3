"""
4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Notice that the solution set must not contain duplicate quadruplets.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [], target = 0
Output: []
 

Constraints:

0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []
        self.backtrack(nums, temp, res, target, 0, 0, 0)
        return res
    
    def backtrack(self, nums, temp, res, target, sm, count, index):
        if count == 4:
            if sm == target:
                res.append(temp[:])
            return
        
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
            if sm + nums[i] + (3 - count)*nums[len(nums) - 1] < target:
                continue
            if sm + (4 - count)*nums[i] > target:
                break
            temp.append(nums[i])
            self.backtrack(nums, temp, res, target, sm + nums[i], count + 1, i + 1)
            temp.pop()