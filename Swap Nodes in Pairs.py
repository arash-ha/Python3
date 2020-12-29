"""
Swap Nodes in Pairs


Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ptr1, ptr2 = head.next, head.next.next
        ptr1.next = head;
        head.next = self.swapPairs(ptr2)
        return ptr1       
    
# Solution 2

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ptr1 = head
        head = head.next
        while ptr1 and ptr1.next:
            ptr2 = ptr1.next.next
            ptr1.next.next = ptr1
            if not ptr2 or not ptr2.next:
                ptr1.next = ptr2
            else:
                ptr1.next = ptr2.next
            ptr1 = ptr2
        
        return head