"""
Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a: int, b: int) -> int:
            return b if a == 0 else gcd(b % a, a)
        d = gcd(len(str1), len(str2))
        return str1[: d] if str1[: d] * (len(str2) // d) == str2 and str2[: d] * (len(str1) // d) == str1 else ''
    