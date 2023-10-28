class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0] * len(s)
        prev,i = 0,1

        while i < len(s):
            if s[i] == s[prev]:
                lps[i] = prev + 1
                prev+=1
                i+=1
            else:
                if prev == 0:
                    i+=1
                else:
                    prev = lps[prev-1]
        l = len(s)
        return s[l-lps[-1]:l]

                    