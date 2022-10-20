class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        for i,n in enumerate(numbers):
            if target-n not in mp:
                mp[n]=i
            else:
                ans = [i+1, mp[target-n]+1]
                ans.sort()
                return ans
            