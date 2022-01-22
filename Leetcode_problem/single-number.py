class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    #brute force
        # for i in nums:
        #     if nums.count(i)<2:
        #         return i
    #xor
        a= 0
        for num in nums:
            a^=num
        return a
        
        
            
        