"""
Majority Element II
Given an integer array of size n, find all elements that appear more than [ n/3 ] times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n, c = len(nums), 1
        if n == 0: return nums
        nums.sort()
        res = []
        prev = nums[0]
        for i in range(1, n):
            if nums[i] == prev: c += 1
            else:
                if c > n//3: res.append(prev)
                c = 1
            prev = nums[i]

        if prev not in nums and c > n//3: res.append(prev)

        return res