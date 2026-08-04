# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        linkedlist -> list of nodes, node: .val, .next
        [0,1,2,3]
        [3,2,1,0] 3->2->1->0->None
        None<-0  1->2->3->None
              
        prev : 1 element behind
        cur : ptr top traverse

        next: next element in list
        next next to cur.next
        set cur.next to prev
        move prev to cur
        move cur to next
        """

        ptr = head
        prev = None

        while ptr:
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp
        
        return prev


        
        