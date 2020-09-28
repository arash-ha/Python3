"""
Word Pattern
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

"""
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        char_map, word_map = {}, {}
        n, i = len(pattern), 0
        words = str.split(" ")
        if n != len(words): return False

        while i < n:
            c, word = pattern[i], words[i]
            if(c in char_map) != (word in word_map): return False
            if c in char_map:
                if (word_map[word] != c) or (char_map[c] != word): return False
            else:
                char_map[c] = word
                word_map[word] = c
            i += 1
        return i == n