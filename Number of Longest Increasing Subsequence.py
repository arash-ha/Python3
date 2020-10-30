"""
Number of Longest Increasing Subsequence

Given an integer array nums, return the number of longest increasing subsequences.
 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

 

Constraints:

0 <= nums.length <= 2000
-106 <= nums[i] <= 106
"""

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n, lis, numLis = len(nums), 1, 0
        length = [1]*n
        count = [1]*n
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

            lis = max(lis, length[i])

        for i in range(n):
            if length[i] == lis:
                numLis += count[i]

        return numLis