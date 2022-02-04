"""
Contiguous Array

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 
Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.

"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0 : -1}
        sm = res = 0
        for i in range(0, len(nums)):
            sm += nums[i] if nums[i] == 1 else -1
            res = max(res, i - mp.setdefault(sm, i))
        return res