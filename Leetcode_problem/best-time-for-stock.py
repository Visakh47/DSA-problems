class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        n = len(prices)
        if n < 2:
            return 0
        
        s,b = prices[1],prices[0]
        profit = s-b
        
        #finding other profit:
        for i in range(0,n):
            b = min(prices[i],b)
            temp = prices[i] - b
            profit = max(temp,profit)
        
        return profit
            
        
        
            