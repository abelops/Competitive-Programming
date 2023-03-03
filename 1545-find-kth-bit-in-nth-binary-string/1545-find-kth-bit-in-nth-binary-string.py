class Solution:
    def invertRev(self, string):
        string = list(string)
        for i in range(len(string)):
            if string[i] == "1":
                string[i] = "0"
            else:
                string[i] = "1"
        # print(string)
        return "".join(string[::-1])
    def customFunc(self, prev, target, k):
        # print(prev, self.invertRev(prev))
        newStr = prev + "1" + self.invertRev(prev)
        if len(newStr) >= k+1:
            return newStr[k]
        return self.customFunc(newStr, target, k)
    def findKthBit(self, n: int, k: int) -> str:
        target = (n * 2) + 1 
        return self.customFunc("0", target, k-1)