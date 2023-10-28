class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = Counter(arr)
        val = sorted(d.values())[::-1]
        print(val)
        out = len(arr)//2
        i = 0
        res=0
        for i in val:
            out -= i
            res +=1
            if out <= 0:
                break
        return res