class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        subArr = []
        def backtrack(start,state):
            if state:
                allOr = reduce(lambda x, y: x | y, state)
                mp[allOr]+=1
                subArr.append(state[:])
                
            for i in range(start, len(nums)):
                state.append(nums[i])
                backtrack(i+1, state)
                state.pop()
        backtrack(0,[])
        return max(mp.values())