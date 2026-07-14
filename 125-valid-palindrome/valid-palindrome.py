class Solution(object):
    def isPalindrome(self, s):
        left=0
        right=len(s)-1
        while left<right:
            while left<right and not s[left].isalnum(): #checks left non char
                left+=1
            while left<right and not s[right].isalnum():
                right-=1 #checks right non char
            
            if s[left].lower()!=s[right].lower():
                return False #lower() converts alphabet to lower so LHS matche RHS
            else:
                left+=1
                right-=1
        return True

