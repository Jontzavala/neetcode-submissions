# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        A = list1
        B = list2
        dummy = ListNode()
        tail = dummy
        while A and B:
            if A.val < B.val:
                tail.next = A
                tail = tail.next
                A = A.next
            elif A.val > B.val:
                tail.next = B
                tail = tail.next
                B = B.next
            else:
                tail.next = A
                tail = tail.next
                A = A.next
        if A:
            tail.next = A
        if B:
            tail.next = B
        return dummy.next

