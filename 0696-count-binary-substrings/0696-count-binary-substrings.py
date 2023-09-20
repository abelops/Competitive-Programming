class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ln = len(s)
        if ln == 1:
            return 0
        ans = 0
        arr = []
        count = 1
        for i in range(1,ln):
            if s[i] == s[i-1]:
                count+=1
            else:
                arr.append(count)
                count = 1
        arr.append(count)
        for i in range(1, len(arr)):
            ans += min(arr[i], arr[i-1])
        return ans
        
                
                
            
        
                