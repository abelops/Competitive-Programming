class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        prefRev = [1]
        inpLength = len(nums)
        rev = inpLength - 1
        for i in range(inpLength):
            pref.append(pref[-1] * nums[i])
            prefRev.append(prefRev[-1] *  nums[rev])
            rev -= 1
        prefRev = prefRev[::-1]
        for i in range(inpLength):
            nums[i] = pref[i] * prefRev[i+1]
        return nums