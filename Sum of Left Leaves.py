"""
Sum of Left Leaves
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0;
        def helper(root, isLeft):
            if isLeft and root.left == None and root.right ==None:
                self.sum += root.val
                return 
            if root.left != None: helper(root.left, True)
            if root.right != None: helper(root.right, False)
        if root == None: return 0
        helper(root, False)
        return self.sum
