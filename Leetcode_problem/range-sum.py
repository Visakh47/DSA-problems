class NumArray:
    #brute force
#     def __init__(self, nums: List[int]):
#         self.nums = nums

#     def sumRange(self, left: int, right: int) -> int:
#         return sum(self.nums[left:right+1])

    def __init__(self, nums: List[int]):
        l = [nums[0]] #prefix sum array
        for i in range(1,len(nums)):
            l.append(l[i-1]+nums[i]) # keep finding the sum at each point
        self.l = l #prefix sum array

    def sumRange(self, left: int, right: int) -> int:
        if (left!=0): #array range is in between 
            return (self.l[right]-self.l[left-1])
        else: #left is 0, we have to find the sum till the right most element -> present in prefix sum position right. 
            return self.l[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)