"""
Subsets II
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtrack(res, [], nums, 0)
        return res
    def backtrack(self, res, temp, nums, index):
        res.append(list(temp))
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]: 
                continue 
            temp.append(nums[i])
            self.backtrack(res, temp, nums, i + 1)
            temp.pop()