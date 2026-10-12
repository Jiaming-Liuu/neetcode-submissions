# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            if fast.next.next == None:
                fast = fast.next
            else:
                fast = fast.next.next
            slow = slow.next
        
        mid = slow.next
        slow.next = None
        prev, nxt = None, mid.next
        while nxt:
            mid.next = prev
            prev = mid
            mid = nxt
            nxt = nxt.next
        mid.next = prev
        
        while mid:
            mid_next = mid.next
            head_next = head.next
            head.next = mid
            mid.next = head_next
            head = head_next
            mid = mid_next