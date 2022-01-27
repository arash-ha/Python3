"""
Maximum XOR of Two Numbers in an Array

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 
Constraints:

1 <= nums.length <= 2 * 10^5
0 <= nums[i] <= 2^31 - 1
"""

class TrieNode:
    def __init__(self):
        self.child = {}

    def increase(self, number):
        cur = self
        for i in range(31, -1, -1):
            bit = (number >> i) & 1
            if bit not in cur.child: cur.child[bit] = TrieNode()
            cur = cur.child[bit]

    def findMax(self, number):
        cur, res = self, 0
        for i in range(31, -1, -1):
            bit = (number >> i) & 1
            if (1-bit) in cur.child:
                cur = cur.child[1 - bit]
                res |= (1 << i)
            else:
                cur = cur.child[bit]
        return res

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trieNode = TrieNode()
        for x in nums:
            trieNode.increase(x)

        res = 0
        for x in nums:
            res = max(res, trieNode.findMax(x))
        return res