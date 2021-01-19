"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 
Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        global max_len, st, end
        max_len, n, st, end = 1, len(s), 0, 0
        
        def getPalindromeLength(l, r):
            global max_len, st, end
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    l, r = l - 1, r + 1
                else:
                    break
                
            ln = r - l - 1
            if ln > max_len:
                max_len = ln
                st, end = l + 1, r - 1
            
        # Odd length
        for i in range(n - 1):
            getPalindromeLength(i, i)
        
        # Even length
        for i in range(n - 1):
            getPalindromeLength(i, i + 1)
        
        return s[st : end + 1]