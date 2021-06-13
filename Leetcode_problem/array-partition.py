from collections import deque
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        t=0
        nums.sort()
        for i in range(0,len(nums),2):
                t = t + nums[i]
        return t