"""
Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.

"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = collections.Counter(s)
        res, visited = [], set()

        for c in s:
            cnt[c] -= 1
            if c in visited:    continue

            while res and res[-1] > c and cnt[res[-1]] > 0:
                visited.remove(res[-1])
                res.pop()
            res.append(c)
            visited.add(c)

        return ''.join(res)