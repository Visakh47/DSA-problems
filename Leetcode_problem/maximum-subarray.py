class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = sum(nums)
        n = len(nums)
        sums = []
        
        for i in range(n+1):
            for j in range(i+1,n+1):
                mx = max(mx,sum(nums[i:j]))
        
        return mx
        
                            
                
                