# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #bruteforce
#         node = head
#         s = []
#         while(node):
#             s.append(node.val)
#             node = node.next
#         print(s)
#         n = len(s)
#         i = 0
#         while( i< n//2 and n!=0 ):
#             if(s[i]!=s[n-1-i]):
#                 return False
#             else:
#                 i = i+1
        
#         return True

        #reverse the linked list but only till the midpoint given by slow

        cur,prev,slow,fast = head,None,head,head
        while(fast and fast.next):
            #each time you break the link and give it back to prev
            cur = slow # putting cur in next node, you want current to be right before slow
            slow = slow.next #slow is used for finding the midpoint and also next node
            fast = fast.next.next
            cur.next = prev # breaking link and giving it to prev
            prev = cur
            
        #slow returns midpoint
        
        #if the LL is odd,then fast will not be null
        if(fast!=None):
            slow = slow.next #we don't need to consider the middle node of odd list
        
        while(cur and slow): #cur is going in reverse, slow is going forward from middle
            if(cur.val!=slow.val):
                return False
            cur = cur.next
            slow = slow.next
        return True
        
            
            
        
        
        
        