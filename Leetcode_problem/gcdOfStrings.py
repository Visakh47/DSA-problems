class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd = ''
        len1 = len(str1)
        len2 = len(str2)
        if len1<len2:
            str1,str2 = str2,str1
            len1,len2 = len2,len1
        

        if str1[0:len2] != str2:
            return ""
        if not str1[len2:]:
            return str1
        return self.gcdOfStrings(str2, str1[len2:])
            
        

                    
            