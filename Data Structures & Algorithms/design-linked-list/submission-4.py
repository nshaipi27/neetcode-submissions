class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.linked_list = None
        

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        curr = self.linked_list
        
        for _ in range(index):
            if curr is None:
                return -1
            curr = curr.next
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        if self.linked_list is not None:
            new_node = Node(val)
            new_node.next = self.linked_list
            self.linked_list = new_node
        else:
            self.linked_list = Node(val)

    def addAtTail(self, val: int) -> None:
        if self.linked_list is None:
            self.addAtHead(val)
        else:
            new_node = Node(val, None)
            curr = self.linked_list
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val, None)
        curr = self.linked_list
        prev = None
        for _ in range(index):
            if curr is None:
                return 
            prev = curr
            curr = curr.next
        new_node.next = curr
        prev.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.linked_list
        prev = None
        for _ in range(index):
            if curr.next is None:
                return
            prev = curr
            curr = curr.next
        prev.next = curr.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)