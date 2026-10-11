class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = []
        for i in range(n):
            parent.append(i)
        
        def find(x):
            while parent[x] != x:
                x= parent[x]
            return x
        def union(i,j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
        
        for i,j in edges:
            union(i,j)
        counter = set()
        for i in range(len(parent)):
            counter.add(find(i))
        print(counter)
        return(len(counter))