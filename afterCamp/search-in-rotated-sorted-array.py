class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l= 0
        r = len(nums)-1
        k = -1
        while l-1 <= r:
            if l == 0:
                l+=1
                r-=1
                continue
            if nums[l-1] > nums[l]:
                k = l
                break
            if nums[r] > nums[r+1]:
                k = r+1
                break
            l+=1
            r-=1
        ans = -1
        if k != -1:
            if nums[k] == target:
                return k
            l = k
            r = len(nums)-1
            while l < r:
                if nums[l] == target:
                    return l
                if nums[r] == target:
                    return r
                mid = (r+l)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
            l = 0
            r = k
            while l < r:
                if nums[l] == target:
                    return l
                if nums[r] == target:
                    return r
                mid = (r+l)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
        
        else:
            l = 0
            r = len(nums)-1
            while l <= r:
                if nums[l] == target:
                    return l
                if nums[r] == target:
                    return r
                mid = (r+l)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return mid
        return ans