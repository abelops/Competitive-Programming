class Trie:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.count = 0
        
    def insert(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] =  Trie()
            cur = cur.children[char]
            cur.count+=1
        cur.is_end = True
    
    def search(self,word):
        cur = self
        tot = 0
        for char in word:
            tot += cur.children[char].count
            cur = cur.children[char]
        return tot
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            ret = trie.search(word)
            ans.append(ret)
        return ans