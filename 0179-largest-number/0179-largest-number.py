class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(map(str, nums), key=LargerNumKey)
        return '0' if nums[0] == '0' else "".join(nums)
        
        