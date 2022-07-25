# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_mid(self , head):
        slow = head
        fast = head.next
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
    def merge(self, left , right):
        if not left:
            return right
        if not right:
            return left
        
        dummy = ListNode(-1)
        curr = dummy
        
        while(left and right):
            if left.val < right.val:
                curr.next = left
                left = left.next
                
            else:
                curr.next = right
                right = right.next
                
            curr = curr.next
                
        curr.next = left or right
        
        return dummy.next
    
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        mid = self.find_mid(head)
        next_to_mid = mid.next
        
        mid.next = None
        
        left = self.sortList(head)
        right = self.sortList(next_to_mid)
        
        return self.merge(left , right)
        
        