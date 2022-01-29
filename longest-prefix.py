class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #prefix is the beginning of the word
        if(len(strs) == 0): return ""
        prefix = ""
        mn = min(strs,key=len)
        for i in range(0,len(mn)):
            temp = []
            for s in strs:
                temp.append(s[i]) # {f,f,f}
            if (len(set(temp) == 1): 
                #we basically check if at all position of i, everyone has the same letter
                prefix = prefix + "".join(set(temp))
            else:
                break

        return prefix
        
                
            
        