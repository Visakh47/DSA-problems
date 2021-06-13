# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        temp = head
        
        l = []
        f = []
        while temp:
            l.append(temp.val)
            temp = temp.next
        
        print(l)
    
        flag = 0
        i = 0
        j = 1
        n = len(l)
        
        for i in range(0,n-1):
            for j in range(i+1,n):
                if(l[i]<l[j]):
                    print("Compared " + str(l[i]) + " and " + str(l[j]))
                    flag = 1
                    f.append(l[j])
                    break
                else:
                    if(flag==1):
                        flag = 0
            if(flag==0):
                f.append(0)
                
                    
           
        
        return f