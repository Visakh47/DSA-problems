class Solution:
    
    def decode(self, encoded: List[int], first: int) -> List[int]:
        a = [first]
        for i in range(0,len(encoded)):
            a.insert(i+1,(encoded[i]^a[i]))
        return a