class Trie:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 27
        self.ind = None
        
    def insert(self, word, ind):
        cur = self
        for char in word:
            pos = ord(char) - ord('a')
            if not cur.children[pos]:
                cur.children[pos] = Trie()
            cur = cur.children[pos]
            cur.ind = ind
        cur.is_end = True
        
        
    def search(self, word):
        cur = self
        for char in word:
            pos = ord(char) - ord('a')
            if not cur.children[pos]:
                return -1
            cur = cur.children[pos]
        return cur.ind
        
        
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i,word in enumerate(words):
            for j in range(len(word)-1,-1,-1):
                self.trie.insert(word[j::]+"{"+word, i)
         

    def f(self, pref: str, suff: str) -> int:
        return self.trie.search(suff+"{"+pref)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)