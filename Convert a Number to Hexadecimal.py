"""
Convert a Number to Hexadecimal

Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Example 1:

Input: num = 26
Output: "1a"

Example 2:

Input: num = -1
Output: "ffffffff"
 
Constraints:

-2^31 <= num <= 2^31 - 1
"""

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        mp = '0123456789abcdef'
        ans = ''
        for i in range(8):
            n = num & 15
            c = mp[n]
            ans = c + ans
            num = num >> 4
        return ans.lstrip('0')