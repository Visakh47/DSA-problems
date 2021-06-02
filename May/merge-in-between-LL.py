class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp1 = ListNode()
        temp1 = list1
        temp2 = ListNode()
        temp2 = list2
        temp3 = ListNode()
            
        f = 0 # for counting postions
        #merging 
        while (f+1!=a):
            temp1 = temp1.next
            f=f+1
            
        first2 = temp2
        while(temp2.next):
            temp2 = temp2.next
        
        
        #temp1 is at a now
        while(f+1<=b):
            temp1.next = temp1.next.next
            f = f+1
        
        
        temp3 = temp1.next
        
        temp1.next = first2
        
        
        while(temp1.next):
            temp1 = temp1.next
        
        temp1.next = temp3
        
        
        mh = list1
        
        return mh