"""
Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 
Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 1:
            return 0
        st = set(nums)
        res = 1
        for n in nums:
            if n not in st:
                continue
            st.remove(n)
            prev, nxt = n - 1, n + 1
            while prev in st:
                prev -= 1
            while nxt in st:
                nxt += 1
            res = max(res, nxt - prev - 1)
        
        return res
