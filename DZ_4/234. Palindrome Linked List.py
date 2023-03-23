# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        start = head
        spis = []
        while start:
            spis.append(start.val)
            start = start.next

        if spis == list(reversed(spis)):
            return True
        return False



    #https://leetcode.com/problems/palindrome-linked-list/