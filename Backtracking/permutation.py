class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        
        def backtrack(temp):
            if len(temp) == len(nums):
                ans.append(temp[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    temp.append(nums[i])
                    visited.add(nums[i])
                    backtrack(temp)
                    temp.pop()
                    visited.remove(nums[i])
                    
        if not nums :
            return ans
        
        backtrack([])
        
        return ans