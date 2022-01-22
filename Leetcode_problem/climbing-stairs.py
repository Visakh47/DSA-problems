class Solution:

    def climbStairs(self, n: int) -> int:
        a,b = 0,1
        c=0 #fibonacci
        if(n<2):
            return n
        else:
            for i in range(0,n):
                c = a + b
                a = b
                b = c
                
        return c