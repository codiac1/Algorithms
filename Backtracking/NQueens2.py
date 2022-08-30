class Solution:
    def totalNQueens(self, n: int) -> int:
        def solve(row ,cols , diag , anti_diag):
            if row == n:
                return 1
            ans =0
            for col in range(n):
                curr_diag = row -col
                curr_anti_diag = row+col
                if col in cols or curr_diag in diag or curr_anti_diag in anti_diag :
                    continue
                cols.add(col)
                diag.add(curr_diag)
                anti_diag.add(curr_anti_diag)
                
                ans += solve(row+1 , cols , diag , anti_diag )
                
                cols.remove(col)
                diag.remove(curr_diag)
                anti_diag.remove(curr_anti_diag)
            return ans
        return solve(0,set(), set(), set())
    