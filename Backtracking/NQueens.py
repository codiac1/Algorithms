class Solution:
    def arrange(self, board):
        newboard = []
        for row in board:
            newboard.append("".join(row))
        return newboard
    
    def can_be_placed(self,row, col ):
        if col not in self.used_col and (row-col) not in self.diag and (row+col) not in self.anti_diag:
            return True
        return False
    
    def placeQueen(self,row , n):
        if row == n:
            nb =self.arrange(self.board)
            #print(nb)
            self.ans.append(nb)
            return 
        for col in range(n):
            if self.can_be_placed(row , col):
                self.board[row][col] = "Q"
                self.used_col.add(col)
                self.diag.add(row-col)
                self.anti_diag.add(row+col)
                
                self.placeQueen(row+1, n)
                
                self.board[row][col] = "."
                self.used_col.remove(col)
                self.diag.remove(row-col)
                self.anti_diag.remove(row+col)
                
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [["."]*(n) for i in range(n)]
        self.ans = []
        self.used_col = set()
        self.diag = set()
        self.anti_diag = set()
        self.placeQueen(0 , n)
        return self.ans
        