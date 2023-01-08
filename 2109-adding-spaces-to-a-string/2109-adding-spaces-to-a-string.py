class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        spaces = set(spaces)
        for i, char in enumerate(s):
            if i in spaces:
                ans.append(" ")
                ans.append(char)
            else:
                ans.append(char)
        return "".join(ans)