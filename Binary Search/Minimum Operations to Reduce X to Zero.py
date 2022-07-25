class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sum_ = sum(nums)
        if sum_ < x :
            return -1
        
        if nums[-1] > x and nums[0] > x:
            return -1
        
        if sum == -x:
            return len(nums)
        
        sum1 = sum_ - x
        i , j , sum2 , max_len = 0 , 0 , 0 , 0
        
        for j in range(len(nums)):
            sum2 += nums[j]
            
            while(i <= j and sum2 > sum1):
                sum2 -= nums[i]
                i += 1
            
            if sum2 == sum1:
                max_len = max(max_len , j-i+1)
        
        return len(nums) - max_len
                
            
            