# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        """

        input: 2 sorted linked lists
        output: single linked list, sorted order of the 2

        ptr for each list
        compare both ptrs, use min to create new list

        in case where 1 list is bigger, append the remaining to the new list

        list1 = [1,2,4], list2 = [1,3,5]
                     .               .
        

        """


        ptr1 = list1
        ptr2 = list2
        node = ListNode(0)
        cur = node

        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                cur.next = ptr1
                ptr1 = ptr1.next
                cur = cur.next
            else:
                cur.next = ptr2
                ptr2 = ptr2.next
                cur = cur.next
        cur.next = ptr1 if ptr1 else ptr2
            

        return node.next


        