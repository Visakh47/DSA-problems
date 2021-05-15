class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums2=[]
        for i in range(0,n):
            nums2.append(nums[i])
            nums2.append(nums[i+n])
        return nums2
        