class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        totLen = len(nums)
        
        def findPivot(l, r):
            tem = l
            pivot = nums[l]
            l+=1
            while True:
                while l <= r and nums[l] <= pivot:
                    l+=1
                while l <= r and nums[r] > pivot:
                    r-=1
                if l <= r:
                    nums[l], nums[r] = nums[r], nums[l]
                else:
                    break
            nums[tem], nums[r] = nums[r], nums[tem]
            return r
                
        def quickSort(l,r):
            if r<=l:
                return nums[r]
            p = findPivot(l, r)
            if p == totLen - k:
                return nums[p]
            if p < totLen - k:
                return quickSort(p+1, r)
            else:  
                return quickSort(l, p-1)

            
        return quickSort(0, totLen-1)
        
            