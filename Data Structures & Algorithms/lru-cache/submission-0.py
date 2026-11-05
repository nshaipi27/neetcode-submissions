class Node:
    def __init__ (self, key = None, val = None, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.keys:
            recent = self.keys[key]
            
            # detach recent
            recent.prev.next = recent.next
            recent.next.prev = recent.prev

            # retach recent to the end of the linked list
            tmp = self.tail.prev 
            self.tail.prev = recent
            tmp.next = recent
            recent.prev = tmp
            recent.next = self.tail
            return self.keys[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            curr_node = self.keys[key]
            curr_node.val = value
            
            # detach curr_node
            tmp = curr_node.prev
            curr_node.prev.next = curr_node.next
            curr_node.next.prev = tmp

            # add to tail
            tmp = self.tail.prev
            self.tail.prev = curr_node
            curr_node.prev = tmp
            curr_node.prev.next = curr_node
            curr_node.next = self.tail
        else:
            new_node = Node(key, value)
            self.keys[key] = new_node

            tmp = self.tail.prev
            self.tail.prev = new_node
            new_node.next = self.tail
            tmp.next = new_node
            new_node.prev = tmp

            if self.capacity < len(self.keys):
                v = self.head.next.key
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.keys[v]
