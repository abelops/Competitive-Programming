class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        mp = defaultdict(list)
        for i in dislikes:
            mp[i[0]].append(i[1])
            mp[i[1]].append(i[0])
        
        color = {}
        
        def recur(cur):
            if cur not in color:
                color[cur] = True
            
            temp = not color[cur]
            for child in mp[cur]:
                if child in color:
                    if color[child] != temp:
                        return False
                    continue
                color[child] = temp
                if not recur(child):
                    return False
            return True
                    
                
        for i in range(1,n+1):  
            if i not in color:
                if not recur(i):
                    return False
                
        return True
            
        
        
        