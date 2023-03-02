"""
Sort an Array

Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 
Constraints:

1 <= nums.length <= 5 * 10^4
-5 * 10^4 <= nums[i] <= 5 * 10^4
"""
# Solution I
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
    
# Solution II
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.mergeSort(nums, n)
        return nums

    def mergeSort(self, A, n):
        if n < 2:
            return
        mid = n // 2
        L, R = [], []
        for i in range(n):
            if i < mid:
                L.append(A[i])
            else:
                R.append(A[i])

        self.mergeSort(L, len(L))
        self.mergeSort(R, len(R))
        self.mergeArrays(A, L, R)

    def mergeArrays(self, A, L, R):
        sizeL, sizeR = len(L), len(R)
        i, j, k = 0, 0, 0
        while i < sizeL and j < sizeR:
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1
        while i < sizeL:
            A[k] = L[i]
            i += 1
            k += 1
        while j < sizeR:
            A[k] = R[j]
            j += 1
            k += 1