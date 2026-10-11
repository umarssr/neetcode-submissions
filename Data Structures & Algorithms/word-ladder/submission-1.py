from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        def differ_by_one(i,j):
            count = 0
            for a,b in zip(i,j):
                if a != b:
                    count +=1
            if count ==1:
                return True
            else:
                return False

        al = defaultdict(list)
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if differ_by_one(wordList[i], wordList[j]):
                    al[wordList[i]].append(wordList[j])
        print(al)

        def bfs(start, end, al):
            visited = set()
            q= deque()
            q.append(start)
            visited.add(start)
            parent = {start: None}
            path = []
            while q:
                node = q.popleft()
                if node == end:
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    return len(path)

                for nei in al[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
                        parent[nei] = node
            return 0
        return bfs(beginWord, endWord, al)
