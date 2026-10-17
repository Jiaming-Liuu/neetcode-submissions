# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        head2 = self.reverseList(slow.next)
        slow.next = None

        while head and head2:
            head_next = head.next
            head2_next = head2.next
            head.next = head2
            head2.next = head_next
            head = head_next
            head2 = head2_next

    def reverseList(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev