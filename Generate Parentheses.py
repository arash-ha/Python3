"""
Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
 
Constraints:

1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(res, cur, c, left, right):
            if c < 0:
                return
            if not left and not right:
                res.append(cur)
                return

            if left:
                helper(res, cur + '(', c + 1, left - 1, right)
            if right:
                helper(res, cur + ')', c - 1, left, right - 1)

        res = []
        helper(res, '', 0, n, n)
        return res