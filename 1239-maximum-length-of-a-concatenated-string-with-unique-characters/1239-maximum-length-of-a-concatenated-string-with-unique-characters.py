class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = set()
        arrLen = len(arr)
        
        def helper(item, state):
            for i in state:
                for j in item:
                    if j in i:
                        return False
            return True
        
        def backtrack(idx, state):
            if state:
                ans.add("".join(state[:]))
            
            for i in range(idx, arrLen):
                if (not state or helper(arr[i], state)) and len(set(arr[i])) == len(arr[i]):
                    state.append(arr[i])
                    backtrack(i+1, state)
                    state.pop()
                
        backtrack(0, [])
        return len(max(list(ans), key=len)) if ans else 0