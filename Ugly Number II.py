"""
Ugly Number II

Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5 = 0, 0, 0
        dp = [1]
        for i in range(1, n):
            p2val = dp[p2] * 2;
            p3val = dp[p3] * 3;
            p5val = dp[p5] * 5;
            cur = min(p2val, p3val, p5val)
            if cur == p2val:
                p2 += 1
            if cur == p3val:
                p3 += 1
            if cur == p5val:
                p5 += 1
            dp.append(cur)
        return dp[n - 1]