"""
Score of Parentheses


Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 
Example 1:

Input: "()"
Output: 1

Example 2:

Input: "(())"
Output: 2

Example 3:

Input: "()()"
Output: 2

Example 4:

Input: "(()(()))"
Output: 6
 

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
"""
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        a, res = 0, 0
        for i in range(len(S) - 1):
            if S[i] == '(':
                if S[i + 1] == ')':
                    res += 1 << a
                a += 1
            else:
                a -= 1
        return res