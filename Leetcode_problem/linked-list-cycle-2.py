# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #brute force, for every node traversed keep true value
        #using floyd cycle algorithm
        #https://www.youtube.com/watch?v=MFOAbpfrJ8g
        #slow moves 1 node, fast moves 2 node
        #if collides, then we reset slow
        #and if it collides again, that's the cycle point 
        
        slow , fast = head, head
        while fast and fast.next: #fast.next is used to check if there is a next node to form cycle or not, if no cycle, then fast.next null
            slow = slow.next
            fast = fast.next.next
            if(slow==fast):
                slow = head
                while slow!=fast:
                    slow = slow.next
                    fast = fast.next    
                return fast #slow collides again
                
            
        
        
            
            