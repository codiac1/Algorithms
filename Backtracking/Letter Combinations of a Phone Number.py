class Solution:
    def helper(self, digits,keypad,curr,idx,n):
        if len(curr) == n:
            self.ans.add(curr[::-1])
            return
        
        for char in keypad[digits[idx]]:
            self.helper(digits,keypad, curr+char ,idx-1 , n)
        
    
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits) 
        if n ==0:
            return set()
        keypad = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        self.ans = set()
        curr = ""
        self.helper(digits ,keypad,curr , n-1 , n)
        return self.ans