"""
Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]

Constraints:

The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
 
Follow-up: Can you solve the problem in O(1) extra memory space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head;
        p = ListNode(-1)
        p.next = head
        cur, nxt, pre = p, p, p
        c = 0
        while cur.next:
            c += 1
            cur = cur.next
        while c >= k:
            cur = pre.next
            nxt = cur.next
            for i in range(1, k):
                cur.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt
                nxt = cur.next

            pre = cur
            c -= k

        return p.next