# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Using Breadth First Search
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        q = [root] #root is set here
        avg = []
        
        while q:
            level = []
            for i in range(len(q)): #New Level Elements
                node = q.pop(0) 
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            avg.append(float(sum(level)/len(level)))
        return avg
        
        
    