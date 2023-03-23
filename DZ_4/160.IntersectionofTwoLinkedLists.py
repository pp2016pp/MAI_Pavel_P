# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return None

        currA = headA
        currB = headB

        while currA != currB:
            if not currA:
                currA = headB
            else:
                currA = currA.next
            if not currB:
                currB = headA
            else:
                currB = currB.next
        return currA

    #https: // leetcode.com / problems / intersection - of - two - linked - lists /