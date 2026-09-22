# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_length = 0
        curr = head
        while curr:
            total_length += 1
            curr = curr.next
        rm_node = total_length - n

        if rm_node == 0:
            return head.next
        
        curr = head
        count = 0

        while count < rm_node - 1:
            curr = curr.next
            count += 1

        curr.next = curr.next.next
        return head
            
        