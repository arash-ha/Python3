"""
Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            sm = carry
            if i >= 0:
                sm += ord(a[i]) - ord('0')
            if j >= 0:
                sm += ord(b[j]) - ord('0')
            i, j = i - 1, j - 1
            carry = 1 if sm > 1 else 0
            res += str(sm % 2)
        if carry:
            res += str(carry)
        return res[::-1]