class Solution:
    def backtrack(self, nums , temp):
        if not nums:
            self.ans.add(tuple(temp[:]))
            return
        for i in range(len(nums)):
            temp =  temp + [nums[i]]
            self.backtrack(nums[:i]+ nums[i+1:] ,temp )
            temp.pop()
            
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        self.backtrack(nums , [])
        return (self.ans)
        