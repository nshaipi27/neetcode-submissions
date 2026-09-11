# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        prev = slow.next = None

        while middle:
            nxt = middle.next
            middle.next = prev
            prev = middle
            middle = nxt
        
        # prev contains the "reversed half" of the list

        order = head
        while prev:
            tmp1 = order.next
            tmp2 = prev.next
            order.next = prev
            prev.next = tmp1
            order, prev = tmp1, tmp2

            

        
