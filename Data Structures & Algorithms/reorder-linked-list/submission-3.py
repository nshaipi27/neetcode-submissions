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
        print(slow.val)
        middle = slow.next
        slow.next = None # detaching step

        prev = None
       
        while middle:
            tmp = middle.next
            middle.next = prev
            prev = middle
            middle = tmp
        
        order = head

        while prev:
            tmp1, tmp2 = order.next, prev.next
            order.next = prev
            prev.next = tmp1
            order = tmp1
            prev = tmp2
        




