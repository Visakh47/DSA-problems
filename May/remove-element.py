class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        nums[:] = (value for value in nums if value != val) #keeps copying the values till it's not equa;
        return len(nums)