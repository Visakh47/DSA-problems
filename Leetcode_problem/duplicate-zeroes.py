class Solution:
    def duplicateZeros(self, nums: List[int]) -> None:
        flag = 0 #initial 
        for i in range(0,len(nums)-1): #only till the second last element 
            if(nums[i] == 0):
                if(flag==1):
                    flag =0
                    continue #skipping the zero
                else : 
                    nums[i+1::] = nums[i:len(nums)-1]
                    flag =1 #value changed , next element is 0