class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solution = []
        
        def backtrack(start, state):
            if sum(state) == target:
                solution.append(state[:])
            elif sum(state) > target:
                return
                
            for i in range(start, len(candidates)):
                state.append(candidates[i])
                if sum(state) < target:
                    backtrack(i, state)
                else:
                    backtrack(i+1, state)
                state.pop()
        backtrack(0, [])
        return solution