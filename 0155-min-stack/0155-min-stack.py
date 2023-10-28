class MinStack:

    def __init__(self):
        self.st = []
        self.min = []

    def push(self, val: int) -> None:
        self.st.append(val)
        old = []
        while self.min and self.min[-1] < val:
            old.append(self.min.pop())
        self.min.append(val)
        self.min.extend(old[::-1])

    def pop(self) -> None:
        self.min.remove(self.st[-1])
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()