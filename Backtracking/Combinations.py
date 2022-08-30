class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(index ,temp ):
            if len(temp)==k:
                ans.append(temp[:])
                return
            for i in range(index, n+1):
                temp.append(i)
                backtrack(i+1,temp)
                temp.pop()
                     
        if k == 1:
            return [[i] for i in range(1 , n+1)]
        ans = []
        backtrack(1,[])
        return ans