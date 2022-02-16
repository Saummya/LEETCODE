# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        node, node_nxt = head, head.next
        while node and node_nxt:
            node.val, node_nxt.val = node_nxt.val, node.val
            node = node_nxt.next
            if node: node_nxt = node.next
        return head
        
 
        