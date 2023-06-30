class Solution:
    def numDecodings(self, s: str) -> int:
        tot = len(s)
        mp = {}
        for i in range(26):
            mp[str(i+1)] = chr(97+i)
        
        def dp(cur,memo, ans):
            if cur == tot:
                ans+=1
                return 1
            if cur in memo:
                return memo[cur]
            temp = 0
            if cur < tot and s[cur] != "0":
                left = dp(cur+1, memo, ans)
                temp+=left
            
            if cur + 1 < tot and s[cur: cur+2] in mp:
                right = dp(cur+2, memo, ans)
                temp+=right
            memo[cur] = temp  
            return temp
                    
        return dp(0, {}, 0)
                