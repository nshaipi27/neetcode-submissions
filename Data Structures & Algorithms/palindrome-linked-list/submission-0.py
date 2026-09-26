# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find middle
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        prev = None
        
        # reverse middle of the list, store it in prev
        while middle:
            tmp = middle.next
            middle.next = prev
            prev = middle
            middle = tmp
        
        # check first half matches prev
        curr = head
        while curr and prev:
            if curr.val != prev.val:
                return False
            curr = curr.next
            prev = prev.next
        return True

