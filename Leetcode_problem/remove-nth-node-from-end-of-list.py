# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #using fast and slow 
        #keep fast n steps ahead, once it reaches, go slow till you reach the end
        slow = head
        fast = head
        for i in range(0,n):
            fast = fast.next
         #so slow is just n steps behind fast and reaches exactly before it needs to remove 
        if(fast):
            while(fast.next):
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
        else:
                head = head.next
        return head
        
        
        
    
            