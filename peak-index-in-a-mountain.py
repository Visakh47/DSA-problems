class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        mid = 0
        while l<=r:
            mid = (l+r)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]<arr[mid+1]:
                l = mid+1
            else:
                r = mid-1
        
        return mid
        
        