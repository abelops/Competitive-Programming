class MapSum:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.prev = -1
        

    def insert(self, key: str, val: int) -> None:
        cur = self
        for char in key:
            if char not in cur.children:
                cur.children[char] = [val, MapSum()]
            else:
                cur.children[char][0] += val
            cur = cur.children[char][1]
            
            
        if cur.is_end:
            prev = cur.prev
            cur = self
            for char in key:
                if char in cur.children:
                    cur.children[char][0] -= prev
                    cur = cur.children[char][1]
        else:
            cur.is_end = True
        cur.prev = val
        
    def sum(self, prefix: str) -> int:
        cur =  self
        ans = 0
        for char in prefix:
            if not char in cur.children:
                return 0
            ans = cur.children[char][0]
            cur = cur.children[char][1]
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)