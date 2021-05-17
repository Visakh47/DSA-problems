class Solution(object):
    def sortArrayByParity(self, nums):
        nums.sort()
        return ([x for x in nums if x%2==0 ] + [x for x in nums if x%2!=0])
        