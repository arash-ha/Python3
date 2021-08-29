"""
Unique Binary Search Trees II

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:

Input: n = 1
Output: [[1]]
 
Constraints:

1 <= n <= 8
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if not n:
            return []

        def helper(low, high):
            vec = []
            if low > high:
                return [None]
            for i in range(low, high + 1):
                left = helper(low, i - 1)
                right = helper(i + 1, high)
                for l in left:
                    for r in right:
                        vec.append(TreeNode(i, l, r))
            return vec

        return helper(1, n)


