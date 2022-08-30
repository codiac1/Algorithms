class Solution:
    def helper(self,start,k,n,temp):
        if k == 0 :
            if n == 0 :
                self.ans.append(temp.copy())
            return
        for i in range(start,10):
            temp.append(i)
            self.helper(i+1 ,k-1, n-i,temp)
            temp.pop()
        
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k == 0:
            return []
        if n < k:
            return []
        self.ans = list()
        self.helper(1,k,n,[])
        return self.ans
        