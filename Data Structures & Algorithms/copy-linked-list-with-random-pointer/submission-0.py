"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        dummy = Node(0)
        p, p1 = head, dummy
        
        while p:
            new_node = Node(p.val)
            p1.next = new_node
            p1 = p1.next
            hashmap[p] = p1
            p = p.next  

        p = head
        while p:
            hashmap[p].random = hashmap.get(p.random)
            p = p.next

        return dummy.next
        