class Solution:    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = (sum(nums) + target)
        if sum(nums)< target or s%2 != 0 or s<0:
            return 0
        s1 = s//2
        dp = [[0]*(s1+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1 
        for i in range(1, n+1):
            for j in range(s1+1):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]