"""
Bitwise AND of Numbers Range

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive. 

Example 1:

Input: left = 5, right = 7
Output:

Example 2:

Input: left = 0, right = 0
Output: 0

Example 3:

Input: left = 1, right = 2147483647
Output: 0

Constraints:

0 <= left <= right <= 231 - 1
"""

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        c = 0
        while not left == right:
            c += 1
            left >>= 1
            right >>= 1
        
        return left << c