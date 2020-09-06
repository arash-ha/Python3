"""
All Elements in Two Binary Search Trees
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]
Example 5:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        s1, s2, res = [], [], []
        while root1 != None or root2!= None or len(s1) > 0 or len(s2) > 0:
            while root1 != None:
                s1.append(root1)
                root1 = root1.left

            while root2 != None:
                s2.append(root2)
                root2 = root2.left

            if len(s2) == 0 or (len(s1) > 0 and s1[-1].val <= s2[-1].val):
                root1 = s1.pop()
                res.append(root1.val)
                root1 = root1.right

            else:
                root2 = s2.pop()
                res.append(root2.val)
                root2 = root2.right

        return res;