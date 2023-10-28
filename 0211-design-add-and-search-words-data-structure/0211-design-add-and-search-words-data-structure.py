class WordDictionary:

    def __init__(self):
        self.is_end = False
        self.children = {}

    def addWord(self, word: str) -> None:
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = WordDictionary()
            cur = cur.children[char]
        cur.is_end = True

    def dfs(self, cur, word, i, l):
        if i < l:
            if word[i] in cur.children:
                return self.dfs(cur.children[word[i]], word, i+1, l)
            elif word[i] != ".":
                return False
            else:
                for child in cur.children:
                    ret = self.dfs(cur.children[child], word, i+1, l)
                    if ret:
                        return True
                return False            
        return cur.is_end
        
        
    def search(self, word: str) -> bool:
        cur = self
        return self.dfs(cur, word, 0, len(word))


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)