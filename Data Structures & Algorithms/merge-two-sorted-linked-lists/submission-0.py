# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        
        lp = list1
        rp = list2

        while lp and rp:
            if lp.val <= rp.val:
                current.next = lp
                lp = lp.next
            else:
                current.next = rp
                rp = rp.next
            
            current = current.next
        
        if lp:
            current.next = lp
        if rp:
            current.next = rp

        return result.next