class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        tot = len(arr)
        i = 0
        c = 0
        while i < len(arr): 
            if arr[i] == 0:
                tot-=1
                bc = arr[i+1:tot+c]
                if i+1 < len(arr):
                    arr[i+1] = 0
                    arr[i+2:]= bc
                i+=2
                c+=1
            else:
                i+=1
        print(arr)
        