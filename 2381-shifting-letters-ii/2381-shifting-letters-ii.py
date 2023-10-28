class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ans = [0] * (len(s) + 1) 
        for start, end, direction in shifts:
            if direction == 1:
                ans[start] += 1
                ans[end+1] -= 1
            else:
                ans[start] -= 1
                ans[end+1] += 1
        for i in range(1, len(ans)):
            ans[i] += ans[i-1]
        chars = list(map(ord, s))
        final = ""
        for i, charInt in enumerate(chars):
            final+=chr(((charInt - ord('a') + ans[i]) % 26) + ord('a'))
        return final