"""
Vertical Order Traversal of a Binary Tree

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
For each node at position (x, y), its left and right children will be at positions (x - 1, y - 1) and (x + 1, y - 1) respectively.
The vertical order traversal of a binary tree is a list of non-empty reports for each unique x-coordinate from left to right. Each report is a list of all nodes at a given x-coordinate. The report should be primarily sorted by y-coordinate from highest y-coordinate to lowest. If any two nodes have the same y-coordinate in the report, the node with the smaller value should appear earlier.
Return the vertical order traversal of the binary tree.
 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: Without loss of generality, we can assume the root node is at position (0, 0):
The node with value 9 occurs at position (-1, -1).
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2).
The node with value 20 occurs at position (1, -1).
The node with value 7 occurs at position (2, -2).

Example 2:

Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report [1,5,6], the node with value 5 comes first since 5 is smaller than 6.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root == None:
            return res
        cache = {}
        self.minC, self.maxC = 0, 0
        
        def dfs(node, r, c):
            if node == None: return
            if c in cache:
                cache[c].append([r, node.val])
            else:
                cache[c] = [[r, node.val]]
            self.minC = min(self.minC, c)
            self.maxC = max(self.maxC, c)
            dfs(node.left, r + 1, c - 1)
            dfs(node.right, r + 1, c + 1)
        
        
        dfs(root, 0, 0)
        
        for c in range(self.minC, self.maxC + 1):
            col = sorted(cache[c], key = lambda x : (x[0], x[1]))
            col_sorted = []
            for p in col:
                col_sorted.append(p[1])
            res.append(col_sorted)
        return res