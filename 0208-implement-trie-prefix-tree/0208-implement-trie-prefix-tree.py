class Trie:

    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]
        

    def insert(self, word: str) -> None:
        cur = self
        for char in word:
            curPos = ord(char) - 97
            if cur.children[curPos] == None:
                cur.children[curPos] = Trie()
            cur = cur.children[curPos]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self
        for char in word:
            curPos = ord(char) - 97
            if cur.children[curPos] == None:
                return False
            cur = cur.children[curPos]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for char in prefix:
            curPos = ord(char) - 97
            if cur.children[curPos] == None:
                return False
            cur = cur.children[curPos]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)