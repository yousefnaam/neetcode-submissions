# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []

        for l in lists:
            cur = l
            while cur:
                heapq.heappush(heap,cur.val)
                cur = cur.next
        dummy = ListNode(0)
        cur = dummy

        while heap:
            val = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next

        

        