class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        mp = {0:0, 1:0}
        piles = deque(piles)
        cur = 0
        while len(piles) > 1:
            left = piles.popleft()
            right = piles.pop()
            mp[1]+=min(left, right)
            mp[0]+=max(left, right)
        return True if mp[0] > mp[1] else False