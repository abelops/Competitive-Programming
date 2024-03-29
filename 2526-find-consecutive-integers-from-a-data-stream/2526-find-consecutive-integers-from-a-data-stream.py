class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.stack = []
        
    def consec(self, num: int) -> bool:
        if num == self.value:
            self.stack.append(num)
        else:
            while self.stack:
                self.stack.pop()
        if len(self.stack) >= self.k:
            return True
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)