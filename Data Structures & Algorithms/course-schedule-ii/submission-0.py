from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = defaultdict(int)
        preqs = prerequisites
        adj_list = defaultdict(list)
        order =[]

        for i, j in preqs:
            indegrees[i] +=1
            adj_list[j].append(i)
        print(indegrees)
        q=deque()
        for i in range(numCourses):
            if i not in indegrees:
                q.append(i)
        while q:
            node = q.popleft()
            order.append(node)
            for nei in adj_list[node]:
                indegrees[nei] -=1
                if indegrees[nei] == 0:
                    q.append(nei)
        for value in indegrees.values():
            if value != 0:
                return []
        return order
            
                    