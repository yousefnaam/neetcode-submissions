# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head

        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next

            if len(stack) == k:
                while stack:
                    prev.next = stack.pop()
                    prev = prev.next
                prev.next = cur
        return dummy.next

            

        