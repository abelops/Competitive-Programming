class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        numLen = len(nums)
        
        def backtrack(ind, state):
            if len(state) > 1:
                if state not in ans:
                    ans.append(state[:])
                
            for i in range(ind, numLen):
                if not state or state[-1] <= nums[i]:
                    state.append(nums[i])
                    backtrack(i+1, state)
                    state.pop()
                
        backtrack(0, [])
        return ans
            