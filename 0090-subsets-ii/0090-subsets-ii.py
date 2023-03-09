class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        def backtrack(start, state):
            if sorted(state) in solutions:
                return
            else:
                solutions.append(sorted(state[:]))
    
            for i in range(start, len(nums)):
                state.append(nums[i])
                backtrack(i+1, state)
                state.pop()
        backtrack(0, [])
        
        return solutions