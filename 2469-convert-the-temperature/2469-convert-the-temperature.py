class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        tk = (celsius + 273.15)
        tf = ((celsius * 9/5) + 32)
        ans.append(tk)
        ans.append(tf)
        return ans