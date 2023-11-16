class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (2*self.n)
        self.build(nums)
        
    def build(self, nums):
        for i in range(self.n):
            self.tree[i+self.n] = nums[i]
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, index: int, val: int) -> None:
        index+=self.n
        self.tree[index] = val
        while index > 0:
            if index % 2 == 0:
                index //= 2
            else:
                index = (index-1)//2
            self.tree[index] = self.tree[index*2] + self.tree[index*2+1]

    def sumRange(self, left: int, right: int) -> int:
        left+=self.n
        right+=self.n
        ans = 0
        while left <= right:
            if left % 2 == 1:
                ans+=self.tree[left]
                left+=1
            if right % 2 == 0:
                ans+=self.tree[right]
                right-=1
            left //= 2
            right //= 2
        return ans
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)