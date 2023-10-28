class Solution:
    def rev(self, l, r, s):
        
        if l == r or l == r+1:
            return s
        s[l], s[r] = s[r], s[l]
        return self.rev(l+1, r-1, s)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return self.rev(0, len(s)-1, s) 