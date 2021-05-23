class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        suml = 0
        n = len(accounts)
        m = len(accounts[0])       
        for i in range(0,n):
            sumt =0 
            for j in range(0,m):
                sumt = sumt + accounts[i][j]
            if(sumt>suml):
                suml = sumt
        return suml