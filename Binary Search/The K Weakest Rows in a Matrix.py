class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def binary_search(row , low , high):
            while(low <= high):
                mid = (low+high)//2
                if row[mid] == 1 :
                    low = mid +1
                else:
                    high = mid -1
            return high +1
        
        for i in range(len(mat)):
            row = mat[i]
            if row[0] == 0:
                mat[i] = 0
            elif row[-1] == 1:
                mat[i] = len(row)
            else:
                mat[i] = (binary_search(row , 0 , len(row)-1))
                
        hp = []
        ans = []
        
        for i in range(len(mat)):
            heappush(hp , (mat[i] , i))
        
        for _ in range(len(hp)):
            s , i = heappop(hp)
            
            ans.append(i)
            
        return ans[:k] 
                
        
            
            
            
            
        
                