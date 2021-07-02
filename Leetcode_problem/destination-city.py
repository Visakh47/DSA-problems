class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        curCity = []
        nextCity = []
        
        for i in range(len(paths)):
            curCity.append(paths[i][0])
            nextCity.append(paths[i][1])
        
        start = paths[0][0]
        
        while ( nextCity[curCity.index(start)] in curCity) :
            start = nextCity[curCity.index(start)]
        
        return nextCity[curCity.index(start)]