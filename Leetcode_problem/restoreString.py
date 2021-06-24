class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        q = ''
        n = [''] * len(s)
        for i in range(0,len(indices)):
            n[indices[i]] = s[i]
        
        for i in n:
            q = q + str(i)
        
        return q