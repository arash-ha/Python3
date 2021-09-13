"""
Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0
 
Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = [0] * 26
        for t in text:
            freq[ord(t) - ord('a')] += 1
        return min(freq[0], freq[1], freq[11] // 2, freq[13], freq[14] // 2)