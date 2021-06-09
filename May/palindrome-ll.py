# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        str1 = []
        while(head!=None):
            str1.append(head.val)
            head = head.next
        
        return(str1==str1[::-1])