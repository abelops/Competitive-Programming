class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        arr = [0] * l
        for i in range(l-1,-1,-1):
            if i == l-1:
                continue
            mini = (float('inf'), -1)
            for j in range(i, i+nums[i]+1):
                if j == l:
                    break
                if arr[j] != 0 or j == l-1:
                    if arr[j] < mini[0]:
                        mini = (arr[j], j) 
            # print(mini)
            if mini[0] != float(inf):
                arr[i] =  arr[mini[1]] + 1
        # print(arr)
        return arr[i]
            