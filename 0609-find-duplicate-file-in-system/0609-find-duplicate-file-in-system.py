class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        
        for i, files in enumerate(paths):
            indFiles = files.split(" ")
            parent = indFiles[0]
    
            for index in range(1,len(indFiles)):
                file = indFiles[index]
                fileNames = file.split("(")
                content = fileNames[1][:-1]
                loc = parent + "/" + fileNames[0]
                words[content].append(loc)
        
        ans = []
        
        for locations in words.values():
            if len(locations) > 1:
                ans.append(locations)
                
        return ans