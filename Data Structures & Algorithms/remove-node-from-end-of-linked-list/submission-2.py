# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        """
        head = [1,2,3,4], n = 2
                  1    2  
        """
        dummy = ListNode(0,head)
        first = dummy
        second = dummy

        for _ in range(n):
            first = first.next
        
        while first and first.next:
            first = first.next
            second = second.next
        second.next = second.next.next

        return dummy.next




        