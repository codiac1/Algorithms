# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        slow = head
        fast = head
        t = k-1
        
        while(t):
            temp = temp.next
            fast = fast.next
            t -= 1
        
        while(fast.next):
            fast = fast.next
            slow = slow.next
        
        slow.val, temp.val = temp.val, slow.val
        return head
        
        