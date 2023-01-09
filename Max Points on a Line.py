"""
Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 
Constraints:

1 <= points.length <= 300
points[i].length == 2
-10^4 <= xi, yi <= 10^4
All the points are unique.
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n
        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            delta_x = x1 - x2
            if delta_x == 0:
                return inf
            return (y1 - y2) / delta_x
        res = 1
        for i, p1 in enumerate(points):
            slopes = collections.defaultdict(int)
            for p2 in points[i + 1:]:
                slope = find_slope(p1, p2)
                slopes[slope] += 1
                res = max(slopes[slope], res)
        return res + 1