class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        l = 0
        r = 1
        s = len(arr)
        c = arr.count(0)
        # while l < s:
        #     # print(l,r)
        #     # print(arr)
        #     if c > 1:
        #         return True
        #     if arr[l] * 2 == arr[r]:
        #         print(arr[l], arr[r])
        #         return True
        #     if arr[l] * 2 < arr[r] and l < r:
        #         l+=1
        #     elif arr[l] * 2 > arr[r] and r < s-1:
        #         r+=1
        #     else:
        #         l+=1
        # return False
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] * 2 == arr[j] and i != j:
                    return True
        return False
            
            
        