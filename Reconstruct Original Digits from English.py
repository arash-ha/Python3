"""
Reconstruct Original Digits from English

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.

Example 1:
Input: "owoztneoer"

Output: "012"

Example 2:
Input: "fviefuro"

Output: "45"
"""

class Solution:
    def originalDigits(self, s: str) -> str:
        n = len(s)
        char = [0] * 26
        nums = [0] * 10
        for i in range(n):
            char[ord(s[i]) - ord('a')] += 1
        while char[ord('z') - ord('a')]:
            nums[0] += 1
            char[ord('z') - ord('a')] -= 1
            char[ord('e') - ord('a')] -= 1
            char[ord('r') - ord('a')] -= 1
            char[ord('o') - ord('a')] -= 1

        while char[ord('w') - ord('a')]:
            nums[2] += 1
            char[ord('t') - ord('a')] -= 1
            char[ord('w') - ord('a')] -= 1
            char[ord('o') - ord('a')] -= 1
        
        while char[ord('u') - ord('a')]:
            nums[4] += 1
            char[ord('f') - ord('a')] -= 1
            char[ord('o') - ord('a')] -= 1
            char[ord('u') - ord('a')] -= 1
            char[ord('r') - ord('a')] -= 1
        
        while char[ord('x') - ord('a')]:
            nums[6] += 1
            char[ord('s') - ord('a')] -= 1
            char[ord('i') - ord('a')] -= 1
            char[ord('x') - ord('a')] -= 1
        
        while char[ord('g') - ord('a')]:
            nums[8] += 1
            char[ord('e') - ord('a')] -= 1
            char[ord('i') - ord('a')] -= 1
            char[ord('g') - ord('a')] -= 1
            char[ord('h') - ord('a')] -= 1
            char[ord('t') - ord('a')] -= 1

        while char[ord('o') - ord('a')]:
            nums[1] += 1
            char[ord('o') - ord('a')] -= 1
            char[ord('n') - ord('a')] -= 1
            char[ord('e') - ord('a')] -= 1
        
        while char[ord('t') - ord('a')]:
            nums[3] += 1
            char[ord('t') - ord('a')] -= 1
            char[ord('h') - ord('a')] -= 1
            char[ord('r') - ord('a')] -= 1
            char[ord('e') - ord('a')] -= 2
        
        while char[ord('f') - ord('a')]:
            nums[5] += 1
            char[ord('f') - ord('a')] -= 1
            char[ord('i') - ord('a')] -= 1
            char[ord('v') - ord('a')] -= 1
            char[ord('e') - ord('a')] -= 1
        
        while char[ord('v') - ord('a')]:
            nums[7] += 1
            char[ord('f') - ord('a')] -= 1
            char[ord('i') - ord('a')] -= 1
            char[ord('v') - ord('a')] -= 1
            char[ord('e') - ord('a')] -= 2
        
        while char[ord('e') - ord('a')]:
            nums[9] += 1
            char[ord('n') - ord('a')] -= 2
            char[ord('i') - ord('a')] -= 1
            char[ord('e') - ord('a')] -= 1
        
        res = ""
        for i in range(10):
            while nums[i]:
                 res += str(i)
                 nums[i] -= 1

        return res