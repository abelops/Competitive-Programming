class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = [0,1]
        def recur(i, count):
            if i < 2:
                if count == 0:
                    return ans[i]
                if count % 2 == 0:
                    return ans[i]
                else:
                    return 0 if ans[i] == 1 else 1
            num = 2
            while num < i+1:
                num *= 2
            return recur(int((i+1 - (num-i+1))/2), count+1)
        return int(recur(k-1, 0))
    
    