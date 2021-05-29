class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ''
        w2 = ''
        #try indexing the array -> faster
        for s in word1:
            w1 = w1 +s
        for q in word2:
            w2 =  w2 +q
        if(w1==w2):
            return True 
        else:
            return False