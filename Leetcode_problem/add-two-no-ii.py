# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Reverse linked list 
        def revLL(head):
            prev = None
            while(head):
                nexthead = head.next
                head.next = prev
                prev = head
                head = nexthead
            return prev
    
        # End of reversing linked list
        
        t1 = l1
        t2 = l2
        l3 = ListNode()
        t3 = l3
        
        c1 = 0
        c2 = 0
        while(t1):
            c1 = c1 + 1
            t1 = t1.next
        while(t2):
            c2 = c2 + 1
            t2 = t2.next
            
        if(c1>c2):  # assigning the longer linked list as t2
            t1 = l2
            t2 = l1
        else:
            t1 = l1
            t2 = l2
            
        t1 = revLL(t1)
        t2 = revLL(t2)
            

        while(t1):
            t3.val = t1.val
            t3.next = ListNode()
            t3 = t3.next
            t1 = t1.next
        
        t3 = l3
        
        c = 0
        
        while(t2):
            t3.val = t3.val + t2.val + c
            c = 0 
            if(t3.val>=10):
                t = t3.val
                c =  t3.val // 10
                t3.val = t%10
            if not (t3.next):
                t3.next = ListNode()
            t3 = t3.next
            t2= t2.next
            
        t3 = l3 
        
        while(t3.next.next):
            t3 = t3.next
            
        if(c!=0):
            t3.next.val = c
        else:
            if(t3.next.val == 0):
                t3.next = None 
        
                
        t4 = revLL(l3)
        return t4