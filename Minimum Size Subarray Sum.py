"""
Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 
Constraints:

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sm, r, l, res = 0, 0, 0, float("inf")
        while r < len(nums):
            while r < len(nums) and sm < target:
                sm += nums[r]
                r += 1
            while sm >= target:
                sm -= nums[l]
                l += 1
            res = min(res, r - l + 1)
        return res if res <= len(nums) else 0
    
    