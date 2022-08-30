class Solution:
    def solve(self, output , op, cp):
        if op == 0 and cp == 0:
            self.ans.append(output)
            return
        if op != 0 and op<cp:
            self.solve(output+"(" , op-1 , cp)
            self.solve(output+")" , op , cp-1)
        else:
            if op == 0 :
                self.solve(output+")" , op , cp-1)
            if op == cp:
                self.solve(output+"(" , op-1 , cp)
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.solve("",n,n)
        return self.ans
        