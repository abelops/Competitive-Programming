class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        pref = [nums[0]]
        prefRev = [nums[-1]]
        ans = []
        for i, j in zip(range(1, len(nums)), range(len(nums)-2, -1, -1)):
            pref.append(pref[-1]+nums[i])
            prefRev.append(prefRev[-1]+nums[j])
        prefRev = prefRev[::-1]
        for i in range(len(pref)):
            ans.append(abs(prefRev[i]-pref[i]))
        return ans