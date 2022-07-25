class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return min(nums[0], nums[1])
        def binary_search(low , high):
            while(low < high):
                mid = (low+high)//2
                
                if nums[mid] > nums[high]:
                    low = mid +1
                else:
                    high = mid
            return nums[low]
        return binary_search(0 , n-1)