class Solution:
    def find_negative_no(self,arr,low,high):
        while(low<high):
            mid = (low+high)//2
            if arr[mid] < 0:
                high = mid
            elif arr[mid] >=0:
                low=mid+1
        
        if arr[low] < 0:
            return (len(arr) - low)
        else:
            return 0
        
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for arr in grid:
            count+=self.find_negative_no(arr,0,len(arr)-1)
        return count
        