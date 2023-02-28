class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.stack = []

    def insertFront(self, value: int) -> bool:
        if(len(self.stack)<self.k):
            if(len(self.stack)==0):
                self.stack.append(value)
            else:
                temp = self.stack
                self.stack = []
                self.stack.append(value)
                self.stack = self.stack + temp
            return True
        else:
            return False
    def insertLast(self, value: int) -> bool:
        if(len(self.stack)<self.k):
            self.stack.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if(len(self.stack)>0):
            self.stack.reverse()
            self.stack.pop()
            self.stack.reverse()
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if(len(self.stack)>0):
            self.stack.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if(len(self.stack)>0):
            return self.stack[0]
        else:
            return -1

    def getRear(self) -> int:
        if(len(self.stack)>0):
            return self.stack[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if(len(self.stack)==0):
            return True
        else:
            return False

    def isFull(self) -> bool:
        if(len(self.stack)==self.k):
            return True
        else:
            return False