class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = int("".join(map(str, digits)))+1
        
        ans = list(str(nums))
        
        ans = list(map(int, ans))
        
        return ans