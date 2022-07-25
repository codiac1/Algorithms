class Solution:
    def b_search_first(self,nums , low, high , target):
        index = -1
        while(low <= high):
            mid = low + (high - low)//2
            if nums[mid] == target:
                index = mid  
                high = mid -1
            elif nums[mid] > target:
                high = mid-1 
            else:
                low = mid+1
        return index
    
    def b_search_last(self,nums , low, high , target):
        index = -1
        while(low <= high):
            mid = low + (high - low)//2
            if nums[mid] == target:
                index = mid
                low = mid+1
            elif nums[mid] > target:
                high = mid -1
            else:
                low = mid+1
        return index
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) == 1 and nums[0] != target:
            return [-1,-1]
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        
        first = self.b_search_first(nums ,0 ,len(nums)-1, target)
        last = self.b_search_last(nums ,0 ,len(nums)-1, target)
        return [first,last]

        
    