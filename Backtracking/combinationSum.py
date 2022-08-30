def combinationalSum(self,arr, target):
        ans = []
        arr = sorted(set(arr))
        def solve(index , target , temp):
            if index == len(arr):
                return  
            if target < 0 :
                return  
            if target == 0:
                ans.append(temp[:])
                return
                
            solve(index +1 , target , temp)
            temp.append(arr[index])
            solve(index , target-arr[index], temp )
            temp.pop()
 
        solve(0 , target , [])
        ans.sort()
        return ans

obj = Solution()
arr = [7, 2, 6, 5]
ans = obj.combinationalSum(arr , 16)
print(ans)
