class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append([nums[i], 0, i])
        
        def merge(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr)//2
            left = merge(arr[:mid])
            right = merge(arr[mid:])
            
            l, r = 0, 0
            lLen = len(left)
            rLen = len(right)
            ans = []
            p = [0] * (lLen)
            c = 0
            while l < lLen and r < rLen:
                if left[l][0] > right[r][0]:
                    # for i in range(l,len(left)):
                    #     left[i][1]+=1
                    c+=1
                    ans.append(right[r])
                    r+=1
                else:
                    left[l][1]+=c
                    ans.append(left[l])
                    l+=1
            while l < lLen:
                left[l][1]+=c
                ans.append(left[l])
                l+=1
            while r < rLen:
                ans.append(right[r])
                r+=1
            # print(left, right, ans)
            return ans
        ret = sorted(merge(ans), key=lambda x: x[2])
        return [x[1] for x in ret] 