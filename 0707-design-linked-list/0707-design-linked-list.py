class node:
    def __init__(self,value):
        self.value = value
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        dummy =self.head
        count = 0
        while dummy:
            if count == index:
                return dummy.value
            dummy = dummy.next
            count += 1
        return -1
    
    def addAtHead(self, val: int) -> None:
        curr = node(val)
        curr.next = self.head
        self.head= curr
        
    def addAtTail(self, val: int) -> None:
        curr = node(val)
        dummy = self.head
        if dummy:
            while dummy.next != None:
                dummy = dummy.next
            dummy.next = curr
        else:
            self.head = curr
            
    def addAtIndex(self, index: int, val: int) -> None:
        newNode = node(val)
        dummy = self.head
        curr = 0
        if index == 0:
            self.addAtHead(val)
        elif dummy:
            while dummy.next != None:
                if curr == index-1:
                    break
                curr += 1
                dummy = dummy.next
            if curr == index-1:
                newNode.next = dummy.next
                dummy.next = newNode
            
    def deleteAtIndex(self, index: int) -> None:
        dummy = self.head
        curr = 0
        if index == 0: 
            if dummy.next is not None:
                self.head = dummy.next
            else:
                self.head = None
        elif dummy:
            while dummy.next is not None:
                if curr == index-1:
                    break
                curr += 1
                dummy = dummy.next
            if curr == index-1:
                if dummy.next is not None:
                    dummy.next = dummy.next.next
            
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)