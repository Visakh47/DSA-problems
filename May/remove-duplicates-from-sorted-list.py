# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp = head
        
        while(temp):
            while temp.next and (temp.val == temp.next.val):
                temp.next = temp.next.next
            temp = temp.next
        
        return head