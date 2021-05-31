class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        def checkFizzBuzz(a):
            if(a%3==0 and a%5==0):
                return "FizzBuzz"
            elif(a%3==0):
                return "Fizz"
            elif(a%5==0):
                return "Buzz"
            else:
                return str(i)
            
        ans = []        
        for i in range(1,n+1): 
            # n+1 as array is only till n-1 
            ans.append(checkFizzBuzz(i))
        
        return ans