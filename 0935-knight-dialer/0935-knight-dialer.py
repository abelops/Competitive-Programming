class Solution:
    def knightDialer(self, n: int) -> int:
        d = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,-1),(-2,1),(2,-1)]
        mat = [[ y*3+1+x for x in range(3)] for y in range(3)]
        mat.append(["*", 0, "*"])
        ans = 0
        
        def inBound(x,y):
            return 0 <= x < 4 and 0 <= y < 3
        memo = {}
        def dp(curX, curY, l):
            if l == n:
                return 1
            
            sums = 0
            if (curX, curY, l) in memo:
                return memo[(curX, curY, l)]
            for px, py in d:
                dx = curX + px
                dy = curY + py
                if inBound(dx, dy) and mat[dx][dy] != "*":
                    sums += dp(dx, dy, l+1)
            memo[(curX, curY, l)] = sums
            return sums
        for i in range(3):
            for j in range(3):
                ans += dp(i,j,1)
        ans+=dp(3,1,1)
                
        return ans % (10**9 + 7)
                
            