class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, r = 0, 0
        stat = -1
        flen = len(haystack)
        slen = len(needle)
        for i in range(flen):
            if haystack[i: i+slen] == needle:
                return i
        return -1