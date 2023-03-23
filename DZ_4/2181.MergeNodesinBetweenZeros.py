# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode(0)
        dummy.next = head
        prev_zero = dummy
        curr = head
        while curr:
            if curr.val == 0:
                sum_nodes = 0
                node_count = 0
                node_list = []
                node = prev_zero.next
                while node != curr:
                    sum_nodes += node.val
                    node_count += 1
                    node_list.append(node)
                    node = node.next
                for node in node_list:
                    prev_zero.next = node
                    prev_zero = prev_zero.next
                prev_zero.next = ListNode(sum_nodes)
                curr = prev_zero.next
            else:
                prev_zero = curr
                curr = curr.next
        node = dummy.next
        while node:
            if node.val == 0:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return dummy.next

# Не получилось, не укладывается во время
# https://leetcode.com/problems/merge-nodes-in-between-zeros/