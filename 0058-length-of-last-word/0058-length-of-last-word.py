class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        
        while s[-1] == "" and s:
            s.pop()
            
        return len(s[-1])