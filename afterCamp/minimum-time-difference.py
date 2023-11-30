class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        l = len(timePoints)
        for i in range(l):
            time, minute = timePoints[i].split(":")
            time, minute = int(time), int(minute)
            timePoints[i] = time * 60 + minute 
        ans = float("inf")
        timePoints.sort()
        for i in range(1,l):
            ans = min(ans, timePoints[i] - timePoints[i-1])
        ans = min(ans, ((24*60) - timePoints[-1]) + timePoints[0])
        return ans
            
        