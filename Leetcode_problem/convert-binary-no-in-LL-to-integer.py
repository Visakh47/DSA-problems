# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def getDecimalValue(self, head: ListNode) -> int:
        temp = ListNode()
        temp = head
        
        if temp.next==None:
            return head.val
        
        c = -1 #starts from -1 as powers starts from 0
        dno = 0
        while (temp!=None):
            c = c+1
            temp = temp.next

        #reintialize temp
        temp = head
        
        while(temp!=None):
            if(temp.val==1):
                dno = dno + pow(2,c) 
            c=c-1
            temp = temp.next
        
        return dno
            