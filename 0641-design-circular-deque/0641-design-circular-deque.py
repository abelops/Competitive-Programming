class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.q = deque()
        self.size = 0
    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.q.appendleft(value) 
            self.size += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.q.append(value)
            self.size += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.q.popleft()
            self.size -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.q.pop()
            self.size -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.q[0]
        else:
            return -1
    def getRear(self) -> int:
        if not self.isEmpty():
            return self.q[-1]
        else:
            return -1
    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()