class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = len(intervals)
        intervals = sorted(intervals)
        ans = [intervals[0]]
        
        for i in range(1, l):
            if ans[-1][1] >= intervals[i][0]:
                poped = ans.pop()
                ans.append([poped[0], max(intervals[i][1], poped[1])])
            else:
                ans.append(intervals[i])
        return ans
    
    
        
        