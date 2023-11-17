# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        low, high = 0, mountain_arr.length()-1
        
        while low < high:
            mid = low + (high - low)//2
            curInd = mountain_arr.get(mid)
            check = mountain_arr.get(mid+1)
            if curInd < check:
                low = mid + 1
            else:
                high = mid

        idx = low
        low, high = 0, idx
        while low < high:
            mid = low + (high - low)//2
            curInd = mountain_arr.get(mid)
            if curInd < target:
                low = mid + 1
            else:
                high = mid
        ans = mountain_arr.get(low)
        
        if ans == target:
            return low
        
        low, high = idx, mountain_arr.length()-1
        while low < high:
            mid = low + (high - low)//2
            curInd = mountain_arr.get(mid)
            if curInd > target:
                low = mid + 1
            else:
                high = mid
        ans = mountain_arr.get(low)
        if ans == target:
            return low
        
        return -1