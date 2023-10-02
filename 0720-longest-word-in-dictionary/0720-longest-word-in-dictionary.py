class Trie:
    def __init__(self):
        self.is_end = False
        self.children = {}
        
    def insert(self, word):
        cur = self
        dif = 0
        for char in word:
            if char not in cur.children:
                dif+=1
            else:
                cur = cur.children[char]
        if dif == 1:
            # print(dif,word, cur.children.keys())
            cur.children[word[-1]] = Trie()
            cur.is_end = True
            return 1
        return 0
            
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        ans = []
        words.sort(key=len)
        for word in words:
            if len(word) == 1:
                ret = trie.insert(word)
                ans.append(word)
                
        for word in words:
            ret = trie.insert(word)
            if ret:
                ans.append(word)

        if not ans:
            return ""
        maxLen = len(max(ans, key=len))
        newAns = list(filter(lambda item: len(item) == maxLen, ans))
        return sorted(newAns)[0]
        
            