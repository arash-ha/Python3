"""
Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false
 
Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.

"""

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helper(s) -> bool:
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return helper(s[i + 1 : j + 1]) or helper(s[i : j])
            i += 1
            j -= 1
        return True