# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        top = None
        if head is None:
            return None
        def reverse(node: ListNode):
            nonlocal top
            if node.next:
                last = reverse(node.next)
                node.next = None
                last.next = node
                return node
            else:
                if top is None:
                    top = node
                return node
            
        reverse(head)
        return top