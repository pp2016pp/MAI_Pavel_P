# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
     start = head
     spis = []
     len = 0
     while start:
         len += 1
         start = start.next
     len = len // 2
     start = head
     for _ in range(len):
        start = start.next
     return start
