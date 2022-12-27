class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        c = 0
        leng = len(nums)
        r = leng-1
        cou = nums.count(val)
        while l < r:
            if nums[l] == val and nums[r]!=val:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                c+=1
                r-=1
                l+=1
            elif nums[l] == val and nums[r]==val:
                c+=1
                r-=1
            elif nums[r]==val:
                r-=1
                l+=1
                c+=1
            else:
                l+=1
        for i in range(cou):
            nums.pop()
        