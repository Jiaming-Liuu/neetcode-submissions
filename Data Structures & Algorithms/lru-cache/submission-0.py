class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # headmap<key, node>
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def _move_to_tail(self, node):
        if node.next == self.tail:
            return
        self._remove(node)
        self._add_to_tail(node)

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        self._move_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self._move_to_tail(node)
        else:
            new_node = ListNode(key, value)
            self.hashmap[key] = new_node
            self._add_to_tail(new_node)
            if len(self.hashmap) > self.capacity:
                to_remove = self.head.next
                self._remove(to_remove)
                del self.hashmap[to_remove.key]