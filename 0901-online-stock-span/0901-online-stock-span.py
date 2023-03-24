class StockSpanner:

    def __init__(self):
        self.stock = [] 

    def next(self, price: int) -> int:
        # print(self.stock)
        if not self.stock:
            self.stock.append((price, 1))
            return 1
        cur = 1
        while self.stock and self.stock[-1][0] <= price:
            temp = self.stock.pop()
            # print(temp)
            cur+= temp[1]
            
        self.stock.append((price, cur))
        return cur

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)