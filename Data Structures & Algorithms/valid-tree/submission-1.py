from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree = no cycles and everything connected
        visited = set()
        al = defaultdict(list)
        for i, j in edges:
            al[i].append(j)
            al[j].append(i)
        def bfs(i):
            q = deque()
            q.append((i, -1))

            while q:
                j, parent = q.popleft()
                visited.add(j)
                for nei in al[j]:
                    if nei == parent:
                        continue
                    if nei in visited:
                        return False
                    q.append((nei, j))
                    visited.add(nei)

            return True
        return bfs(0) and len(visited)== n
        
