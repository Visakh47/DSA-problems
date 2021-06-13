class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums2=[]
        for i in nums:
            if i not in nums2: #not in condition
                nums2.append(i)
        nums[0:len(nums2)] = nums2[0:len(nums2)]
        return len(nums2)