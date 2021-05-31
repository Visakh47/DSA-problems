class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        itemso = ["type","color","name"]
        
        n = itemso.index(ruleKey)
        
        c = 0
        for i in range(len(items)):
            if(ruleValue==items[i][n]):
                c= c+1
        
        return c