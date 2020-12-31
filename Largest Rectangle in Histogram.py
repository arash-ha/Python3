"""
Largest Rectangle in Histogram


Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        size = len(heights)
        stk = []
        i, maxArea = 0, 0
        while i < size:
            if(not stk or heights[i] >= heights[stk[-1]]):
                stk.append(i)
                i += 1
            else:
                h = stk.pop()
                maxArea = max(maxArea, heights[h] * (i if not stk else i - stk[-1] - 1))

        return maxArea