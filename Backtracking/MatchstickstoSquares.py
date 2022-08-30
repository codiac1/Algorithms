class Solution:
    def makesquare(self, matchbox: List[int]) -> bool:
        
        
        if len(matchbox) < 4:
            return False
        sum_  = sum(matchbox)
        
        if sum_%4 != 0:
            return False
        
        matchbox.sort(reverse = True)
        
        side1 ,side2, side3, side4 = 0,0,0,0
        index = 0 
        side_len = sum_/4
        dp = {}
        
        def dfs(side1 , side2 , side3 , side4 , index ):
            if side1> side_len or side2>side_len or side3>side_len or side4>side_len:
                return False
        
            if index == len(matchbox):
                return side1 == side2 ==side3 == side4
            
                
            if (side1 , side2 , side3 , side4 , index) in dp:
                return dp[(side1 , side2 , side3, side4,index)]
            
            dp[(side1 , side2 , side3, side4,index)] = dfs(side1+matchbox[index] , side2 , side3 ,side4, index+1) or dfs(side1, side2+matchbox[index]  , side3 ,side4, index+1) or dfs(side1 , side2 , side3+matchbox[index] ,side4 ,index+1) or dfs(side1 , side2 , side3 ,side4 +matchbox[index], index+1)
            
            
            return dp[(side1 , side2 , side3, side4 , index)]
        
        
        return dfs(side1 , side2 , side3 , side4 , index)