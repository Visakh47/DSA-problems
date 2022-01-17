def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        for d in digits:
            num = num + str(d)
         
        num = int(num) + 1
        
        num = str(num)
        
        #use list comprehension
        res = [int(x) for x in num]
        
        return res
        