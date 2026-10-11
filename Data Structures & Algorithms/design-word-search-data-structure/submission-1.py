class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = WordDictionary()
            node = node.children[c]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self
        def dfs(i, node):
            if i == len(word):
                return node.end_of_word
            c = word[i]
            if c == ".":
                for child in node.children.values():
                    if dfs(i+1, child):
                        return True
                return False
            if c not in node.children:
                return False
            return dfs(i+1, node.children[c])
        return dfs(0,node)
        
