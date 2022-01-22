class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums2 = []
        nums2 = set(nums)
        da = []
        for i in range(1,len(nums)+1):
            if i not in nums2:
                da.append(i)
                
        return da
                
                