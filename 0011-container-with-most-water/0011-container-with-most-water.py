class Solution:
    def maxArea(self, height: List[int]) -> int:
        ma = 0 
        l = 0
        r = len(height)-1
        
        while l < r:
            area = min(height[l],height[r]) * (r - l)
            ma = max(area, ma)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return ma