"""
Add Two Numbers II


You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import itertools
from collections import deque

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        st1, st2 = deque(), deque()

        while l1:
            st1.append(l1.val)
            l1 = l1.next

        while l2:
            st2.append(l2.val)
            l2 = l2.next

        carry = 0
        base = 10
        current_node = ListNode(carry)

        for terms in itertools.zip_longest(reversed(st1), 
                                           reversed(st2), 
                                           fillvalue=0):
            current_sum = sum(terms) + carry
            current_node.val = current_sum % base
            carry = current_sum // base
            head = ListNode(carry)
            head.next = current_node
            current_node = head

        return current_node if current_node.val != 0 else current_node.next 