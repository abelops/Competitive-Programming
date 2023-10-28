class Solution(object):
    def validateStackSequences(self, pushed, popped):
        d = 0
        stack = []
        for i in pushed:
            stack.append(i)
            while(stack and d < len(popped) and stack[-1]==popped[d]):
                stack.pop()
                d+=1
        return d==len(pushed)
    