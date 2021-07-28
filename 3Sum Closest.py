"""
3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2). 

Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff, prevDiff = 0, 2**(31) - 1 

        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                diff = abs(target - sm)
                if(diff < prevDiff):
                    prevDiff = diff
                    res = sm

                if sm == target:
                    return sm
                if sm < target:
                    l += 1
                else:
                    r -= 1

        return res