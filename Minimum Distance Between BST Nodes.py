"""
Minimum Distance Between BST Nodes

Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Example 1:

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1
 
Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 10^5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res, data = float("inf"), -1
        def solve(root):
            nonlocal data, res
            if not root: return
            solve(root.left)
            if data != -1:
                res = min(res, root.val - data)
            data = root.val
            solve(root.right)
        solve(root)
        return res