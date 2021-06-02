# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        
        #we reach the node before a 
        
        
        # assigning the first of the second linked list 
        first2 = temp2
        while(temp2.next):
            temp2 = temp2.next
            
        #traversed to the end of second node 
        
        
        #temp1 is still at ath node 
        # in given loop , till the position is less than or equal to b , we remove the nodes in between and increment the postion in list 
        while(f+1<=b):
            temp1.next = temp1.next.next
            f = f+1
        
        
        #final nodes left over at first linked list, where the link is stored in temp3
        
        temp3 = temp1.next
        
        #attaching the end of the first linked list to the second linked list 
        temp1.next = first2
        
        
        #traverse till end of the merged list 
        while(temp1.next):
            temp1 = temp1.next
        
        # link the end of the merged list with left over nodes from list1
        temp1.next = temp3
        
        
        mh = list1
        
        return mh