"""
Array of Doubled Pairs

Given an array of integers arr of even length, return true if and only if it is possible to reorder it such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2. 

Example 1:

Input: arr = [3,1,3,6]
Output: false

Example 2:

Input: arr = [2,1,2,6]
Output: false

Example 3:

Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

Example 4:

Input: arr = [1,2,4,16,8,4]
Output: false
 
Constraints:

0 <= arr.length <= 3 * 10^4
arr.length is even.
-10^5 <= arr[i] <= 10^5
"""
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        ump = Counter(arr)
        arr.sort()
        for a in arr:
            if ump[a] == 0:
                continue
            if a < 0 and a % 2 != 0:
                return False
            b = a * 2 if a > 0 else a // 2
            if ump[b] == 0:
                return False
            ump[a] -= 1
            ump[b] -= 1
        return True