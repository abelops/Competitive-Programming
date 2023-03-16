class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = sorted([ar[0], ar[1], i] for i, ar in enumerate(intervals))
        def binSearch(arr):
            l = 0 
            r = len(intervals) - 1
            ret = []
            while l <= r:
                mid = l + (r-l)//2
                if arr[1] > intervals[mid][0]:
                    l = mid + 1 
                else:
                    r = mid - 1
                    ret.append(intervals[mid])
            if ret:
                return min(ret)[2]
            return -1   
        ans = []
        for i in sorted(intervals, key= lambda x:x[-1]):
            stat = binSearch(i)
            if stat != -1:
                ans.append(stat)
            else:
                ans.append(-1)
        return ans