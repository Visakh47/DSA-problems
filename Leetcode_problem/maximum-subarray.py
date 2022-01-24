class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#         mx = sum(nums)
#         n = len(nums)
#         sums = []
        
#         for i in range(n+1):
#             for j in range(i+1,n+1):
#                 mx = max(mx,sum(nums[i:j]))
        
#         return mx
    
        #implementing kadane's algorithm
        current_max = nums[0]
        highest_max = nums[0]
        
        for i in range(1,len(nums)):
            current_max = max(nums[i],current_max+nums[i])
            highest_max = max(current_max,highest_max)
        
        return highest_max
        
                            
                
                