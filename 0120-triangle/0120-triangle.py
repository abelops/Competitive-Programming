class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        leng = len(triangle)
        if leng == 1:
            return triangle[0][0]
        minn = float("inf")
        def dp(cur, level, memo):
            # print(cur, level)
            if level == leng-1:
                return triangle[-1][cur]
            
            if (cur, level) in memo:
                return memo[(cur, level)]
            ans = float("inf")
            for i in range(cur, level+1):
                left = dp(cur+1, level+1, memo) 
                right = dp(cur, level+1, memo) 
                ans = min(left, right)
            ans += triangle[level][cur]
            memo[(cur, level)] = ans
            return ans
                
        return dp(0, 0,{})