class Solution:    
    def maxArea(self, nums: List[int]) -> int:
        wid = len(nums)-1
        i = 0
        j = wid
        max_area = 0
        while(i<j):
            area = min(nums[i],nums[j]) * wid
            max_area = max(max_area , area)
            if nums[i] < nums[j]:
                i += 1
            else:
                j -= 1
            wid -= 1
        return max_area