"""
Three Equal Parts

You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.
If it is possible, return any [i, j] with i + 1 < j, such that:
arr[0], arr[1], ..., arr[i] is the first part,
arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
All three parts have equal binary values.
If it is not possible, return [-1, -1].
Note that the entire part is used when considering what binary value it represents. For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.

Example 1:

Input: arr = [1,0,1,0,1]
Output: [0,3]

Example 2:

Input: arr = [1,1,0,1,1]
Output: [-1,-1]

Example 3:

Input: arr = [1,1,0,0,1]
Output: [0,2]
 
Constraints:

3 <= arr.length <= 3 * 104
arr[i] is 0 or 1
"""

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        s = sum(arr)
        if not s: return [0, len(arr) - 1]
        if s % 3: return [-1, -1]

        count = a = b = c = -1
        for i, n in enumerate(arr):
            if not n: continue
            count += 1
            a = i if a < 0 else a
            if count == s // 3:
                c = i if b > 0 else -1
                b = i if b < 0 else b
                count = 0

        while c < len(arr) and arr[a] == arr[b] == arr[c]:
            a, b, c = a + 1, b + 1, c + 1

        return [a - 1, b] if c == len(arr) else [-1, -1]