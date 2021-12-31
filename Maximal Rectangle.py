"""
Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:

Input: matrix = []
Output: 0

Example 3:

Input: matrix = [["0"]]
Output: 0

Example 4:

Input: matrix = [["1"]]
Output: 1

Example 5:

Input: matrix = [["0","0"]]
Output: 0
 
Constraints:

rows == matrix.length
cols == matrix[i].length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not len(matrix) or not len(matrix[0]):
            return 0
        rows, cols, maxArea = len(matrix), len(matrix[0]), 0
        h = [0] * (cols + 1)
        for i in range(rows):
            lowi = []
            for j in range(cols + 1):
                h[j] = h[j] + 1 if (j != cols and matrix[i][j] == '1') else 0
                while(lowi and (h[j] < h[lowi[-1]])):
                    height = h[lowi[-1]]
                    lowi.pop()
                    lefti = -1 if not lowi else lowi[-1]
                    maxArea = max((j - lefti - 1) * height, maxArea)
                lowi.append(j)
        return maxArea