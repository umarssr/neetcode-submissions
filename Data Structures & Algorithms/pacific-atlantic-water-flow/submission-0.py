from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_queue = deque()
        p_seen = set()

        a_queue = deque()
        a_seen = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        rows, cols = len(heights), len(heights[0])
        for j in range(cols):
            p_queue.append((0, j))
            p_seen.add((0,j))

        for i in range(1,rows):
            p_queue.append((i, 0))
            p_seen.add((i,0))

        for i in range(rows):
            a_queue.append((i, cols-1))
            a_seen.add((i, cols-1))
        
        for j in range(cols-1):
            a_queue.append((rows-1, j))
            a_seen.add((rows-1, j))

        def get_coords(que, seen):
            coords = set()
            while que:
                i, j = que.popleft()
                for di, dj in directions:
                    r,c = i+di, j+dj
                    if 0 <= r<rows and 0<=c<cols and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append((r,c))
        get_coords(p_queue, p_seen)
        get_coords(a_queue, a_seen)
        return list(p_seen.intersection(a_seen))

