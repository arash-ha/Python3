"""
Sum of Subarray Minimums

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 
Constraints:

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        s, res = [-1], 0
        arr += [0]
        for i, n in enumerate(arr):
            while arr[s[-1]] > n:
                j, k = s.pop(), s[-1]
                res += (j - k)*(i - j) * arr[j]
            s.append(i)
        return res % 1000000007