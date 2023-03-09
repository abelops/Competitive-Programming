class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def comb(start, cur):
            if len(cur) == k:
                ans.append(cur[:])
                return
            for i in range(start, n+1):
                cur.append(i)
                comb(i+1, cur)
                cur.pop()
        comb(1, [])
        return ans
    
    