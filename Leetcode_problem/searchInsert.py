class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            pos = 0
            for i in range(len(nums)):
                if (target>nums[i]):
                    pos = pos + 1
                else:
                    return pos
            return pos


# Another Approach

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if(target in nums):
#             return nums.index(target)
#         nums.append(target)
#         nums.sort()
#         return nums.index(target)