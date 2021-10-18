"""
Cousins in Binary Tree

Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
 

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 
Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = [root]
        x_level = 0
        y_level = 0
        curr_level = -1
        while q:
            curr_level += 1
            l = len(q)
            for _ in range(l):
                cur = q.pop(0)
                if cur.val == x:
                    x_level = curr_level
                if cur.val == y:
                    y_level = curr_level
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                if cur.left and cur.right:
                    if (cur.left.val == x and cur.right.val == y) or (cur.left.val == y and cur.right.val == x):
                        return False

        return x_level == y_level