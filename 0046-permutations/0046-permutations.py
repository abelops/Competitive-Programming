class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        numLen = len(nums)
        def perm(n,cur):
            if len(cur) == numLen:
                if len(set(cur)) == numLen:
                    ans.append(cur.copy())
                return
            for i in range(numLen):
                # if nums[i] != nums[n]:
                cur.append(nums[i])
                perm(i, cur)
                cur.pop()
        perm(1,[])
        return ans