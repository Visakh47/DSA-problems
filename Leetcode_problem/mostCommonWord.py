class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count = 0
        paragraph = paragraph.replace(',',' ').replace(';',' ').replace('!',' ').replace('?',' ').replace("'",' ').replace('.',' ').split(' ')
        
        for i in range(0,len(banned)):
            banned[i] = banned[i].lower()
        
        for i in range(0,len(paragraph)):
            paragraph[i] = paragraph[i].lower()
        
        ubw = [x for x in paragraph if x not in banned]
        
       
                
        maxval = 0
        maxp = 0
        c =0
        print(ubw)
        if len(ubw)==1:
            return ubw[0].lower()
        for i in range(0,len(ubw)):
            if(ubw[i]!=''):
                c = ubw.count(ubw[i])
                if(c>maxval):
                    maxval = c
                    maxp = i
        
        return ubw[maxp]
            