"""
Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:

Input: s = ""
Output: 0
 
Constraints:

0 <= s.length <= 3 * 10^4
s[i] is '(', or ')'.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []
        st.append(-1)
        maxL = 0
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    maxL = max(maxL, i - st[-1])

        return maxL