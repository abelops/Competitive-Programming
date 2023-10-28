class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        newGoal = goal+goal
        lps = [0] * len(s)
        
        prev, i = 0, 1
        
        while i < len(s):
            if s[prev] == s[i]:
                lps[i] = prev + 1
                i+=1
                prev+=1
            else:
                if prev == 0:
                    i+=1
                else:
                    prev = lps[prev-1]
        i, j = 0, 0
        while i < len(s) and j < len(newGoal):
            if s[i] == newGoal[j]:
                i+=1
                j+=1
            else:
                if i > 0:
                    i = lps[i-1]
                else:
                    j+=1
        if i == len(s):
            return True
        return False
                    