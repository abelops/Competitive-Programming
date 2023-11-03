class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        while True:
            if i not in arr:
                k-=1
            if k == 0:
                return i
            i+=1