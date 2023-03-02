class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for p, s in sorted(zip(position, speed)):
            time.append(float(target - p)/s)
        ans = cur = 0
        time = time[::-1]
        for t in time:
            if t > cur:
                ans += 1
                cur = t
        return ans
        