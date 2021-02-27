"""
Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Example 3:

Input: dividend = 0, divisor = 1
Output: 0

Example 4:

Input: dividend = 1, divisor = 1
Output: 1
 
Constraints:

-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0

"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == -2147483648 and divisor == -1):
            return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for x in range(31, -1, -1):
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (dividend > 0) == (divisor > 0) else -res