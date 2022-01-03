class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Brute force solution 
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    return list([i,j])
        

        #Match No Solution
        for i in range(0,len(nums)):
            match_no = target - nums[i]
            try:
                j = nums.index(match_no)
            except:
                print("not found")
            if match_no in nums and i!=j:
                return list([i,j])