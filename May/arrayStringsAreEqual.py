class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        finalw1 = ''
        finalw2 = ''
        for s in word1:
            finalw1 = finalw1 +s
        for q in word2:
            finalw2 =  finalw2 +q
        if(finalw1==finalw2):
            return True 
        else:
            return False