# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        a = list1
        b = list2
        while a and b:
            if a.val < b.val:
                tail.next = a
                tail = tail.next
                a = a.next
            else:
                tail.next = b
                tail = tail.next
                b = b.next
        if not a:
            tail.next = b
        elif not b:
            tail.next = a
        return dummy.next