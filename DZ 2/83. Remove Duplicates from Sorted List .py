# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Function to remove duplicates in a sorted list 
        start = head
        if not head:
            return head
        while start.next is not None:
            if start.val == start.next.val:
                start.next = start.next.next
            else:
                start = start.next

        return head