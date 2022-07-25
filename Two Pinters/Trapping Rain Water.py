class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        right = [0]*n
        lh = 0
        rh = 0
        water = 0
        
        for i in range(n):
            left[i] = max(height[i], lh)
            lh = left[i]
            
        for i in range(n-1 , -1, -1):
            right[i] = max(height[i], rh)  
            rh = right[i]
        
        for index in range(n):
            water += min(left[index] , right[index]) - height[index]
        return water
            