class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # 1,3,5,7,9
        # 0,2,4,6,8
        # -4,-2,2,4
        # 6,2,2,1
        mp = Counter(arr)
        if mp[0] % 2 == 1:
            return False
        arr = sorted(mp.keys(), reverse=True)
        c = 0
        for i in range(len(arr)):
            # print(i)
            if mp[arr[i]] == 0 or arr[i] == 0:
                continue
                
            if arr[i] < 0:
                if arr[i] * 2 not in mp or mp[arr[i]] > mp[arr[i]*2]:
                    return False
                else:
                    mp[arr[i] * 2]-= mp[arr[i]]    
            else:
                if arr[i] / 2 not in mp or mp[arr[i]] > mp[arr[i]/2]:
                    return False
                else:
                    mp[arr[i] / 2]-= mp[arr[i]]
        return True