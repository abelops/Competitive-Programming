class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = int("".join(list(map(str, num)))) + k
        ans = []
        for i in str(s):
            ans.append(int(i))
        return ans