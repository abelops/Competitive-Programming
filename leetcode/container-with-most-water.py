class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ma = 0
        while(r>l):
            area = (r-l)*min(height[l], height[r])
            if(area > ma):
                ma=area
            if(height[l]>height[r]):
                r-=1
            else:
                l+=1
                
        return ma