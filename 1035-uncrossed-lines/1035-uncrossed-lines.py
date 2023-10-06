class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        l1,l2 = len(nums1), len(nums2)
        memo = {}
        def dp(first,second):
            if first > l1 and second > l2:
                return 0
            if (first,second) in memo:
                return memo[(first, second)]
            curMax = 0
            for i in range(first, l1):
                for j in range(second, l2):
                    # print(i, j, nums1[i], nums2[j])
                    if nums1[i] == nums2[j]:
                        left = dp(i+1, j+1)+1
                        # right = dp(first, second+1)
                        curMax = max(curMax, left)
                        # print(i, j, curMax)
            memo[(first,second)] = curMax
            return curMax
    
        return dp(0,0)
        