class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        output = float("inf")       
        q = deque()
        q.append([0, -1])
        total = 0
        for i in range(n):
            total += nums[i]
            while len(q) and total - q[0][0] >= k:
                [runningSum, index] = q.popleft()
                output = min(output, i - index)
            while len(q) and total < q[-1][0]:
                q.pop()            
            q.append([total, i])
            
        return -1 if output == float("inf") else output