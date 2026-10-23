class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = node.prev = None

    def _move_to_tail(self, node):
        self._remove_node(node)
        self._add_to_tail(node)

    def _add_to_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self._move_to_tail(self.hashmap[key])
            return self.hashmap[key].value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self._move_to_tail(self.hashmap[key])
            self.hashmap[key].value = value
        else:
            new_node = ListNode(key, value)
            self._add_to_tail(new_node)
            self.hashmap[key] = new_node
            if len(self.hashmap) > self.cap:
                node_to_remove =  self.head.next
                self._remove_node(node_to_remove)
                del self.hashmap[node_to_remove.key]