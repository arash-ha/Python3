"""
Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted(nums)
        self.backtrack(res, [], nums, 0)
        return res
    
    def backtrack(self, res, temp, nums, index):
        res.append(list(temp))
        for i in range(index, len(nums)):
            temp.append(nums[i])
            self.backtrack(res, temp, nums, i + 1)
            temp.pop()
