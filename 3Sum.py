"""
3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return {}
        nums.sort()
        res = []
        for i in range(n - 1):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            low, high = i + 1, n-1
            while low < high:
                sm = nums[i] + nums[low] + nums[high]
                if sm == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    left = nums[low]
                    while low < high and left == nums[low]:
                        low += 1
                    right = nums[high]
                    while low < high and right == nums[high]:
                        high -= 1

                elif sm > 0:
                    high -= 1
                else:
                    low += 1

        return res