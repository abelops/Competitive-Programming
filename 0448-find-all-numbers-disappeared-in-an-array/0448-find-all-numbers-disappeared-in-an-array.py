class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [-1] * len(nums)
        for i in nums:
            # print(i-1)
            arr[i-1] = i
        return [x+1 for x in range(len(arr)) if arr[x] == -1]
    