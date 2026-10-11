from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board), len(board[0])
        starts = []
        locked = set()
        # left side appending
        for i in range(rows):
            if board[i][0] == "O" and (i,0) not in starts:
                starts.append((i,0))
                locked.add((i,0))
        # right side appending
        for i in range(rows):
            if board[i][cols-1] == "O" and (i,cols-1) not in starts:
                starts.append((i,cols-1))
                locked.add((i, cols-1))
        # top appending
        for j in range(cols):
            if board[0][j] == "O" and (0, j) not in starts:
                starts.append((0,j))
                locked.add((0,j))
        # bottom appending
        for j in range(cols):
            if board[rows-1][j] == "O" and (rows-1,j) not in starts:
                starts.append((rows-1,j))
                locked.add((rows-1, j))
        q = deque(starts)
        while q:
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            r,c = q.popleft()
            for dr, dc in directions:
                if 0<=r+dr<rows and 0<=c+dc<cols and board[r+dr][c+dc] == "O" and (r+dr,c+dc) not in locked:
                    locked.add((r+dr, c+dc))
                    q.append((r+dr, c+dc))
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i,j) not in locked:
                    board[i][j] ="X"

