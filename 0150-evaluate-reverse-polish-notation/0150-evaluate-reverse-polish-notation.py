class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opps = set(['+', '-', '*', '/'])
        stack = []
        for i in tokens:
            if i not in opps:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()

                if i == '+':
                    c = a+b
                if i == '-':
                    c = a - b
                if i == '*':
                    c = a*b
                if i == '/':
                    c = int(a/b)
                stack.append(c)
        return stack[0]