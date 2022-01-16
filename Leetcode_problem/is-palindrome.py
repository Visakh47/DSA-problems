class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # lr=''
        # rl=''
        # #converting to a string:
        # str1 = str(x)
        # for i in str1
        #     lr = lr + i
        # for j in reversed(str1):
        #     rl = rl + j
        # print(rl)
        # print(lr)
        # print(str1)
        # if(lr == rl and lr == str1):
        #     return True
        
        
        #solution using modulus
        #take a rem, divby 10
        # num1 = x
        # rl = 0
        # while(num1>0):
        #     rl = rl*10 + num1%10;
        #     num1 = num1//10
        # if(rl == x):
        #     return True
        
        #best space time complexity:
        
        str_x = str(x)
        return str_x == str_x[::-1] #reversing the string with index array functions
            
            
        