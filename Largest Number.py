"""
Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.

"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if(len(nums) == 0): return ""
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                A = str(nums[i]) + str(nums[j])
                B = str(nums[j]) + str(nums[i])
                if int(A) < int(B): nums[i], nums[j] = nums[j], nums[i]
        
        allZero = True
        res = ""
        for num in nums:
            if num != 0: allZero = False
            res += str(num) 
            
        if(allZero): return "0"
        
        return res