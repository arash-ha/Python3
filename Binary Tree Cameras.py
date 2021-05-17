"""
Binary Tree Cameras

Given a binary tree, we install cameras on the nodes of the tree. 
Each camera at a node can monitor its parent, itself, and its immediate children.
Calculate the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:

Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:

Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.cam = 0
        def dfs(root):
            if not root:
                return 2
            l, r = dfs(root.left), dfs(root.right)
            if l == 0 or r == 0:
                self.cam += 1
                return 1
            return 2 if l == 1 or r == 1 else 0
        return (dfs(root) == 0) + self.cam