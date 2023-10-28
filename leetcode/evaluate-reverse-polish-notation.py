class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if(i!='+' and i!='-' and i!='*' and i!='/'):
                stack.append(i)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if(i=='+'):
                    stack.append(int(num2)+int(num1))
                elif (i=='-'):
                    stack.append(int(num2)-int(num1))
                elif (i=='*'):
                    stack.append(int(num2)*int(num1))
                elif (i=='/'):
                    stack.append(int(int(num2)/int(num1)))
        return stack.pop()