class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3=[]
        nums1= set(nums1)
        nums2= set(nums2)
        for i in nums1:
            if i in nums2:
                nums3.append(i)
        return nums3
            