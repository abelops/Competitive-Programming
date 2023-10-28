class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        miss = []
        mp = {}
        mis=0
        fin = []
        prev = None
        for i in range(len(nums)):
            if i+1 not in nums:
                mis = i+1
                if prev == "rep":
                    fin.append(mis)
                    prev = "nf"
                else:
                    miss.append(mis)
            if nums[i] not in mp:
                mp[nums[i]] = i
            else:
                if prev == None or prev == "nf":
                    fin.append(nums[i])
                    prev = "rep"
                    if miss:
                        an = miss.pop()
                        fin.append(an)
                        prev = "nf"
                else:
                    fin.append(miss[-1])
                    ans.append(nums[i])
                    prev = "rep"
                fin
                mis=0
        return fin