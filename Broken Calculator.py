
"""
Broken Calculator

On a broken calculator that has a number showing on its display, we can perform two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.

Example 1:

Input: X = 2, Y = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

Example 2:

Input: X = 5, Y = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.

Example 3:

Input: X = 3, Y = 10
Output: 3
Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.

Example 4:

Input: X = 1024, Y = 1
Output: 1023
Explanation: Use decrement operations 1023 times.
 
Note:

1 <= X <= 10^9
1 <= Y <= 10^9
"""
# Solution I
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X == Y:
            return 0
        if X > Y:
            return X - Y
        if Y % 2:
            return 1 + self.brokenCalc(X, Y + 1)
        else:
            return 1 + self.brokenCalc(X, Y // 2)
        
# Solution II

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        res = 0
        while startValue < target:
            target = target + 1 if target % 2 > 0 else target // 2
            res += 1
        return res + startValue - target