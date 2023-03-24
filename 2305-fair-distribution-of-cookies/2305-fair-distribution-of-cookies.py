class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float("inf")
        def backtrack(n, state):
            nonlocal ans
            if n >= len(cookies):
                # print(state)
                ans = min(ans, max(state))
                return
            if max(state) >= ans:
                return
            for i in range(k):
                state[i]+=cookies[n]
                backtrack(n+1, state)
                state[i]-=cookies[n]
        if len(cookies) == k:
            return max(cookies)
        backtrack(0,[0]*k)
        return ans