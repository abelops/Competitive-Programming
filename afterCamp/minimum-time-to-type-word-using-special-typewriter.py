class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 0
        cur = 'a'
        for char in word:
            ans += min(abs(ord(char) - ord(cur)), ord(min(char, cur)) - 97 + ord('z') - ord(max(char,cur))+1)
            ans+=1
            cur = char
        return ans