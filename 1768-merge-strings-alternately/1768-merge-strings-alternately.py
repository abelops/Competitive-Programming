class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        long = max(word1, word2, key=len)
        ans = ""
        for i in range(len(long)):
            if i < len(word1):
                ans+=word1[i]
            if i <len(word2):
                ans+=word2[i]
        return ans