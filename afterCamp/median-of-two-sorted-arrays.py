class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        l, r = 0, 0
        tot = len(nums1) + len(nums2)
        if tot == 1:
            return (nums1 + nums2)[0]
        if tot == 2:
            return ((nums1 + nums2)[0] + (nums1 + nums2)[1])/2
        if tot == 3:
            return sorted((nums1 + nums2))[1]
            
        even = tot % 2 == 0
        counts = 0
        mid = tot//2
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                arr.append(nums1[l])
                l+=1
            else:
                arr.append(nums2[r])
                r+=1
            if even:
                if counts == mid:
                    return (arr[-1] + arr[-2])/2
            else:
                if counts == mid:
                    return arr[-1]
            counts+=1
        # print(arr)
        for i in range(l, len(nums1)):
            if even:
                if counts == mid:
                    return (arr[-1] + nums1[i])/2
            else:
                if counts == mid:
                    return nums1[i]
            arr.append(nums1[i])
            counts+=1
        # print(mid,r, counts)
        for i in range(r, len(nums2)):
            # print(arr, counts)
            if even:
                if counts == mid:
                    return (arr[-1] + nums2[i])/2
            else:
                if counts == mid:
                    return nums2[i]
            arr.append(nums2[i])
            counts+=1
            