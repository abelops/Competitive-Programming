class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1 = s
        text2 = s[::-1]
        len1 = len2 = len(s)
        mat = [[0] * (len2+1) for x in range(len1+1)]
        for i in range(len1-1,-1,-1):
            for j in range(len2-1, -1, -1):
                if text1[i] == text2[j]:
                    mat[i][j]= 1 + mat[i+1][j+1]  
                else:
                    mat[i][j]= max(mat[i+1][j], mat[i][j+1])
        return mat[0][0]
        