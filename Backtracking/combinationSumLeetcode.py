class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return 0
        
        ans = []
        
        def combi_sum(index , temp , target):
            if index == len(candidates):
                return 
            
            if target == 0:
                ans.append(temp[:])
                return 
                
            if target < 0:
                return 
            
            #not taking the ith element
            
            combi_sum(index+1 , temp , target)
            
            #taking the ith element
            
            temp.append(candidates[index])
            combi_sum(index , temp , target-candidates[index])
            
            #backtracking step
            
            temp.pop()
            
        combi_sum(0 , [], target)
        
        return ans