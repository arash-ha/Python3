"""
Permutations II


Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(l):
            myset = set()
            if l == n:
                result.append(nums[:])
            for i in range(l, n):
                if nums[i] not in myset:
                    myset.add(nums[i])
                    nums[i], nums[l] = nums[l], nums[i]
                    backtrack(l + 1)
                    nums[i], nums[l] = nums[l], nums[i]

        backtrack(0)
        return result