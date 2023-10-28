class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        
        for i, tem in enumerate(temperatures):
            while(stack != [] and tem > stack[-1][0]):
                te, prev = stack.pop()
                ans[prev] = i - prev
            stack.append([tem,i])  
            print(stack)
        return ans


    