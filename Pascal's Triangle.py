"""
Pascal's Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""
#Solution I
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result, path = [], [1]
        for i in range(numRows):
            result.append(path)
            path = [1] + [path[j] + path[j+1] for j in range(len(path)-1)] + [1]
        return result
    
# Solution II
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res