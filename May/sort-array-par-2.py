class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = [x for x in nums if x%2==0]
        even = [x for x in nums if x%2!=0]
        nums2= []
        for i in range(0,len(nums)//2):
            nums2.append(odd[i])
            nums2.append(even[i])
        return nums2
            