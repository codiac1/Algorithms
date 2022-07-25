# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return head
        slow = head
        fast = head
        temp = slow
        
        while(fast):
            if not fast.next:
                break
            fast = fast.next.next
            temp = slow
            slow = slow.next
        if temp == slow:
            return slow.next
        temp.next = slow.next
        return head
            