class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        wordLength = len(words)
        charIndex = {}
        
        for char in range(len(order)):
            charIndex[order[char]]=char
            
        for i in range(wordLength - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if charIndex[words[i][j]] > charIndex[words[i+1][j]]:
                        return False
                    break
            
        return True
