class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        
        for i, files in enumerate(paths):
            indFiles = files.split(" ")
            loc = [indFiles[0]]
            loc.append("/")
            
            for index in range(1,len(indFiles)):
                file = indFiles[index]
                fileNames = file.split("(")
                content = fileNames[1][:-1]
                loc.append(fileNames[0])
                words[content].append("".join(loc))
                loc.pop()
        
        ans = []
        
        for locations in words.values():
            if len(locations) > 1:
                ans.append(locations)
                
        return ans