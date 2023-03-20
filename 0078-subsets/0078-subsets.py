class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        def backtrack(start, cur):
            nonlocal solutions
            if cur not in solutions:
                solutions.append(cur[:])
            if len(cur) == len(nums):
                return
                
            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(i+1, cur)
                cur.pop()
        backtrack(0, [])
        
        return solutions
    
    