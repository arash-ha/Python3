"""
Word Ladder

Given two words beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Return 0 if there is no such transformation sequence.

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
 

Constraints:

1 <= beginWord.length <= 100
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the strings in wordList are unique.
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordDict = set(wordList)
        visited = set([beginWord])
        toVisit = collections.deque([(beginWord, 1)])
        while toVisit:
            word, k = toVisit.popleft()
            if word == endWord:
                return k
            for i in range(len(word)):
                for j in range(26):
                    char = ord('a') + j
                    new_word = word[0 : i] + chr(char) + word[i + 1 :]
                    if new_word in wordDict and new_word not in visited:
                        visited.add(new_word)
                        toVisit.append((new_word, k + 1))
        return 0