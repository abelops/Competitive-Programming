class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ans = [intervals[0]]
        l = len(intervals)
        if l == 1:
            return ans
        for i in range(1, len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                poped = ans.pop()
                ans.append([poped[0], max(intervals[i][1], poped[1])])
            else:
                ans.append(intervals[i])
        return ans