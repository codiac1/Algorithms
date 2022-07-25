class Solution:
    def find_mountain(self ,arr, low , high):
        while(low<high):
            mid= (low+high)//2
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                low = mid
            else:
                high = mid
                
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        return self.find_mountain(arr , 0,n)