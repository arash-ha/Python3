"""
Sort an Array

Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000

"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.quickSort(nums, 0, n-1)
        return nums
    def quickSort(self, nums, low, high):
        if low < high: 
            pivot = self.partition(nums, low, high)
            self.quickSort(nums, low, pivot - 1)
            self.quickSort(nums, (pivot + 1), high)

    def partition (self, nums: List[int], low, high) -> int:
        i = (low - 1)
        pivot = nums[high]
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return (i + 1)