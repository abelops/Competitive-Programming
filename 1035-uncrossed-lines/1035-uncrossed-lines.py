class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        l1,l2 = len(nums1), len(nums2)
        if l1 > l2:
            nums2.extend([0]*(l1-l2))
        elif l2 > l1:
            nums1.extend([0]*(l2-l1))
        
        l = max(l1, l2)
        mat = [[ 0 for x in range(l+1)] for y in range(l+1)]
        
        for i in range(l-1, -1, -1):
            for j in range(l-1, -1, -1):
                if nums1[i] == nums2[j]:
                    mat[i][j] = mat[i+1][j+1] +1
                else:
                    mat[i][j] = max(mat[i+1][j], mat[i][j+1])
        return mat[0][0]
        