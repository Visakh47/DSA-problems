class Solution:
    def letterCombinations(self, digits: str) -> List[str]:   
        #recursive soln using hashmaps
        ra= []
        hm = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        #the length of each string will be equal to the length of digits
        # ex digits = [2,3]
        
        def recur(i, curr):
            if len(curr) == len(digits): # base case of recursion. 
                ra.append(curr)
                return
            else: #forming the currrent string 
                for c in hm[digits[i]]:
                    recur(i+1,curr+c)
            
        if digits:
            recur(0,'')
        return ra
        