# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        d1 = ListNode(-1)
        d2 = ListNode(-1)
        dm1 = d1
        dm2 = d2
    
        while(head != None ):
            if(head.val <x):
                dm1.next = head
                dm1= head
            else:
                dm2.next = head
                dm2 = head 
            head = head.next
        dm2.next=None
        dm1.next = d2.next
        return d1.next
        
            