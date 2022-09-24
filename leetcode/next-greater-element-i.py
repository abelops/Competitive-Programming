class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            m = -1
            for j in range(nums2.index(i), len(nums2)):
                if(nums2[j]>i):
                    m=nums2[j]
                    break
            res.append(m)
        return res