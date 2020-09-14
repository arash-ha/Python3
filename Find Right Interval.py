"""
Find Right Interval
Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
 

Example 1:

Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
 

Example 2:

Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
 

Example 3:

Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.

"""


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted = []
        n = len(intervals)
        for i  in range(n):
            sorted.append([intervals[i], i])

        sorted.sort()

        result = [-1]*n

        def binary_search(x):
            if sorted[n - 1][0][0] < x : return -1
            l = 0
            r = n - 1
            while l <= r:
                mid = l + (r - l)//2
                if sorted[mid][0][0] >= x: r = mid - 1
                else: l = mid + 1
            return sorted[l][1]


        for i in range(n):
            result[i] = binary_search(intervals[i][1])

        return result

