"""
Reshape the Matrix

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix. 

Example 1:

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
 
Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
"""

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not len(mat) * len(mat[0]) == r * c:
            return mat
        if len(mat) == 0 or len(mat[0]) == 0:
            return mat
        tmp = []
        res = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                tmp.append(mat[i][j])

        k = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = tmp[k]
                k += 1

        tmp.clear()
        return res