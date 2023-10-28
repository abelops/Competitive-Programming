class Trie:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26
        
    def insert(self, word):
        cur = self
        for char in word:
            pos = ord(char) - ord('a')
            if not cur.children[pos]:
                cur.children[pos] = Trie()
            cur = cur.children[pos]
        cur.is_end = True
        
    
        
    def search(self, word, s):
        cur = self
        curIdx, idx = 0, 0
        l = len(s)
        while curIdx < l and idx < len(word):
            wPos = ord(word[idx]) - ord('a')
            sPos = ord(s[curIdx]) - ord('a')
            if cur.children[wPos]:
                idx += 1
            curIdx+=1
            cur = cur.children[sPos]
        return 1 if idx == len(word) else 0
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        trie.insert(s)
        ans = 0
        found = defaultdict(int)
        for word in words:
            if word in found:
                if found[word]:
                    ans+=1
                continue
            res = trie.search(word,s)
            found[word] = res
            ans+=res
        return ans