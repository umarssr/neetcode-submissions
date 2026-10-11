from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = prerequisites
        indegrees = defaultdict(int)
        for i,j in preqs:
            indegrees[i] +=1
        q= deque()
        al = defaultdict(list)
        for i,j in preqs:
            al[j].append(i)
        for i in range(numCourses):
            if i not in indegrees:
                q.append(i)
        while q:
            node = q.popleft()
            for nei in al[node]:
                indegrees[nei] -=1
                if indegrees[nei] == 0:
                    q.append(nei)
        for value in indegrees.values():
            if value != 0:
                return False
        return True

         
