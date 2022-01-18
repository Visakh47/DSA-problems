class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2 != 0:
            return False
        elif (s[0]==')' or s[0]==']' or s[0] == '}'):
            return False
        else:
            for ch in s:
                if(ch=='(' or ch == '{' or ch == '['):
                    stack.append(ch)
                elif(ch==')'):
                    if(stack and stack.pop() == '('):
                        continue
                    else:
                        return False
                elif(ch=='}'):
                    if(stack and stack.pop() == '{'):
                        continue
                    else:
                        return False
                elif(ch==']'):
                    if(stack and stack.pop() == '['):
                        continue
                    else:
                        return False 
            if not stack:
                return True
            
                
    
                    
                
                
            
                
                    
                