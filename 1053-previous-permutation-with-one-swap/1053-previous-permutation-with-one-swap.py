class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        leng = len(arr)
        temp = (-1,-1)
        for i in range(leng-2,-1,-1):
            if arr[i+1] < arr[i]:
                temp = (arr[i], i)
                break
        if temp[0] == -1:
            return arr
        for j in range(leng - 1, temp[1], -1):
            if arr[j] < arr[temp[1]] and arr[j] != arr[j - 1]:
                arr[j], arr[temp[1]] = arr[temp[1]], arr[j]
                break
        return arr