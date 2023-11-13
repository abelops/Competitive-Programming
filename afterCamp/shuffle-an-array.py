class Solution:

    def __init__(self, nums: List[int]):
        self.orgi = list(nums)
        self.arr = nums

    def reset(self) -> List[int]:
        self.arr = self.orgi
        self.orgi = list(self.orgi)
        return self.arr 

    def shuffle(self) -> List[int]:
        for i in range(len(self.arr)):
            idx = random.randrange(i, len(self.arr))
            self.arr[i], self.arr[idx] = self.arr[idx], self.arr[i]
        return self.arr
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()