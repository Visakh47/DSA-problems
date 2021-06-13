class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        i = 1
        mno = []
        while(len(mno)!=k):
            if i in nums:
                i = i+1
                continue
            else:
                mno.append(i)
                i = i+1
        return mno[-1]
                