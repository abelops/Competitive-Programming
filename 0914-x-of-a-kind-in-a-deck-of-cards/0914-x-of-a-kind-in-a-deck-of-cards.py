class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        mp = Counter(deck)
        reps = reduce(gcd, set(mp.values()))
        return True if reps > 1 else False