class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for i in range(len(board)):
            rowcheck = set()
            for j in range(len(board)):
                if board[i][j] != "." and board[i][j] in rowcheck:
                    return False
                else:
                    rowcheck.add(board[i][j])
        #cols
        for i in range(len(board)):
            colcheck = set()
            for j in range(len(board)):
                if board[j][i] !="." and board[j][i] in colcheck:
                    return False
                else:
                    colcheck.add(board[j][i])
        #boxes
        starts = [(0,0), (0,3), (0,6), 
                  (3,0), (3,3), (3,6),
                  (6,0), (6,3),(6, 6)]
        for i,j in starts:
            boxcheck = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    if board[row][col] != "." and board[row][col] in boxcheck:
                        return False
                    else:
                        boxcheck.add(board[row][col])
        return True

