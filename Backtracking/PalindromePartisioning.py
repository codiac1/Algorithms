class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        def isPalindrome(s , start , end):
            while(start <= end):
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
                
            return True                
        
        def helper(index , temp):
            if index == len(s):
                ans.append(temp[:])
                return 
            
            for i in range(index , len(s)):
                if isPalindrome(s , index , i):
                    temp.append(s[index : i+1])
                    helper(i+1 , temp)
                    temp.pop()
                    
        helper(0 , [])
        
        return ans 