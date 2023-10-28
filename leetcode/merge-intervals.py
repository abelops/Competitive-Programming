class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals)==1):
            return intervals
        intervals.sort()
        newList = intervals
        result = []
        for i in newList:
            if(len(result)==0):
                result.append(i)
            else:
                if(result[-1][1]>=i[0]):
                    result[-1][1] = max(result[-1][1], i[1])
                else:
                    result.append(i)
        return result