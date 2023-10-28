class Solution:
    def freqAlphabets(self, s: str) -> str:
        '''
            1. Create the hashmap to store the characters and values
            2. itterate through the given string and store the values on a string
            3. return the string
        '''
        a = ord('a')
        mp = {}
        counter = 1 
        for i in range(a, a+9):
            mp[str(counter)] = chr(i)
            counter+=1
        j = ord('j')
        counter = 10
        for l in range(j, j+17):
            mp[str(counter)+"#"] = chr(l)
            counter+=1
        ans = ""
        l = len(s)-1
        c = 0
        while(l>=0):
            if s[l]=="#":
                ans+=mp[s[l-2:l+1]]
                # print(s[l-2:l+1])
                l-=3
            else:
                ans+=mp[str(s[l])]
                # print(s[l])
                l-=1
        return ans[::-1]
                
        