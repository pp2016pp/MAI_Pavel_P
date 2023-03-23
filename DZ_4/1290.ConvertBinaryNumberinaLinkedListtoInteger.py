# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:


        decimal = 0
        while head:
            # shift the current decimal value to the left by 1 bit and add the current bit
            decimal = (decimal << 1) | head.val
            head = head.next
        return decimal


# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/