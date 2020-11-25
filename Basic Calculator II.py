"""
Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        a = 0
        op = '+'
        s += '+'
        for c in s:
            if c.isdigit():
                a = a*10 + int(c)
            elif c == ' ':
                continue
            else:
                if op == '+':
                    stack.append(a)
                elif op == '-':
                    stack.append(-a)
                elif op == '*':
                    op1 = stack.pop()
                    stack.append(op1*a)
                elif op == '/':
                    op1 = stack.pop()
                    stack.append(math.trunc(op1/a))
                a = 0
                op = c
                    
        return sum(stack)