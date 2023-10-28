class Solution:
    def countVowels(self, word: str) -> int:
        ans = 0
        vowels = set(['a','e','i','o','u'])
        n = len(word)
        for i,char in enumerate(word):
            if char in vowels:
                ans += (i + 1) * (n-i)
        return ans
            