class Solution:
    def checkIfExist(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num*2 in s or num/2 in s:
                return True
            else:
                s.add(num)
        return False
    