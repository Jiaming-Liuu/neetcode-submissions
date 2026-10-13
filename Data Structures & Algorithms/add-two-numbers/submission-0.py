# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 and l2:
            cur_val = l1.val + l2.val + carry
            carry = 0
            if cur_val > 9:
                carry = 1
                cur_val -= 10
            cur_l = ListNode(cur_val)
            cur.next = cur_l
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        if l1 or l2:
            if l1: cur.next = l1
            else: cur.next = l2
            if carry:
                cur.next.val += 1
        elif carry:
            cur.next = ListNode(1)

        return dummy.next