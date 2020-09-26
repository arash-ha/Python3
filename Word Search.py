"""
Word Search
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def checkValid(word, m, n) -> bool:
            if len(word) == 0: return True
            if m < 0 or m >= len(board) or n < 0 or n >= len(board[0]) or board[m][n] != word[0]: return False
            c = board[m][n]
            board[m][n] = '*'
            s = word[1:]
            v = checkValid(s, m - 1, n) or checkValid(s, m + 1, n) or checkValid(s, m, n - 1) or checkValid(s, m, n + 1)
            board[m][n] = c
            return v
        
        for m in range(len(board)):
            for n in range(len(board[m])):
                if(checkValid(word, m, n)): return True

        return False
