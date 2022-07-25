class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        def binary_search(low , high):
            while(low <= high):
                mid = ( low + high )//2
                
                if numbers[mid] == ele :
                    return mid

                elif numbers[mid] > ele :
                    high = mid -1
                    
                else:
                    low = mid +1 
            return -1
        
        
        for i in range(0 , n):
            ele = target - numbers[i]
            
            idx = binary_search(i+1 , n-1)
            
            if idx != -1:
                return [i+1 ,idx+1 ]
        