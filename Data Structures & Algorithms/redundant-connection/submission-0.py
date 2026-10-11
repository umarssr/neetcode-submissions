class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = []
        for i in range(len(edges)+1):
            parent.append(i)
        
        def find(x):
            while parent[x] !=x:
                x = parent[x]
            return x
        def union(i,j):
            find_i = find(i)
            find_j = find(j)
            if find_i != find_j:
                parent[find_i] = find_j
            else:
                return [i,j]
        for i,j in edges:
            res = union(i,j)
            if res:
                return res
        