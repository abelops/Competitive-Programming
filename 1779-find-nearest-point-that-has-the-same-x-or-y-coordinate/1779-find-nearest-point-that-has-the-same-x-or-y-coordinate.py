class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        relatedPoints = []
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                dist = abs(points[i][0]-x) + abs(points[i][1]-y)
                relatedPoints.append([dist,i])
        if len(relatedPoints)==0:
            return -1
        return min(relatedPoints, key=lambda x: x[0])[1]
        
        