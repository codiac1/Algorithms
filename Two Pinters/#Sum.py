class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0 :
            return []    
        nums.sort()
        ans = []
        i = 0
        for i in range(n):
            if( i > 0 and nums[i] == nums[i-1]):
                continue
            target = -nums[i]
            low = i+1
            high = n-1
            
            while(low<high):
                curr_sum = nums[low] + nums[high]
                if curr_sum == target:
                    ans.append([nums[i], nums[low], nums[high]])
                    low += 1
                    #high -= 1
                              
                    while low<high and nums[low] == nums[low-1]:
                        low += 1
                    while low<high and nums[high] == nums[high-1]:
                        high -= 1
                    
                elif curr_sum > target:
                    high -= 1
                else:
                    low += 1
        return ans
                

                
                