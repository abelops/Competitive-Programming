class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill = sorted(skill)
        l = 0
        r = len(skill)-1
        gap = skill[r] + skill[l]
        ans = 0
        while l < r:
            if skill[r] + skill[l] != gap:
                return -1
            ans+=skill[r] * skill[l]
            l+=1
            r-=1
        return ans