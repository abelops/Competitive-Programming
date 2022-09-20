class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack1 = []
        stack2 = []
        for i in s:
            if(i!=')'):
                stack1.append(i)
            else:
                d = stack1.pop()
                while(d!="("):
                    stack2.append(d)
                    d = stack1.pop()
                stack1 = stack1 + stack2
                stack2 = []
        return "".join(stack1)
            
        