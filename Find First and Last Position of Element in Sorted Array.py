"""
Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 
Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1] * 2
        n = len(nums) - 1

        def binarySearch(l, h, b) -> int:
            res = -1
            while l <= h:
                mid = (l + h) // 2      
                if nums[mid] == target:
                    res = mid
                    if(b):
                        l = mid + 1
                    else:
                        h = mid - 1
                elif nums[mid] > target:
                    h = mid - 1
                else:
                    l = mid + 1
            return res

        res[0] = binarySearch(0, n, False)
        res[1] = binarySearch(0, n, True)
        return res
