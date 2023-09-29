class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        l = len(s)
        text1 = s
        text2 = s[::-1]
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i < l and j < l:
                if text1[i] == text2[j]:
                    temp = dp(i+1, j+1)
                    memo[(i,j)] = temp + 1
                    
                else:
                    left = dp(i+1, j)
                    right = dp(i, j+1)
                    memo[(i,j)] = max(left, right)
                return memo[(i,j)]
            return 0
        return dp(0,0)
            
        # text1 = s
        # text2 = s[::-1]
        # len1 = len2 = len(s)
        # mat = [[0] * (len2+1) for x in range(len1+1)]
        # for i in range(len1-1,-1,-1):
        #     for j in range(len2-1, -1, -1):
        #         if text1[i] == text2[j]:
        #             mat[i][j]= 1 + mat[i+1][j+1]  
        #         else:
        #             mat[i][j]= max(mat[i+1][j], mat[i][j+1])
        # return mat[0][0]
        