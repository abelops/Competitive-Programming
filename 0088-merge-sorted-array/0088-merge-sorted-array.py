class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m - 1     # The end of the first list
        right = n + m -1 # The end of the 0's in the first list
        middle = n -1    # The end of the second list
        
        while middle >=0:
            if left >=0 and nums1[left] > nums2[middle]:
                nums1[right] = nums1[left]
                left -= 1
                right -= 1
            else:
                nums1[right] = nums2[middle]
                middle -= 1
                right -= 1