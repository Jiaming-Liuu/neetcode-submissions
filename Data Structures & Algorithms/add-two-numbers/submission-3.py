# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        carry = 0
        p1, p2, p3 = l1, l2, dummy
        while p1 or p2 or carry:
            p1_val = p1.val if p1 else 0
            p2_val = p2.val if p2 else 0
            val = p1_val + p2_val + carry
            carry = val // 10
            val = val - 10 if carry else val

            new_node = ListNode(val)
            p3.next = new_node
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            p3 = p3.next
        
        return dummy.next