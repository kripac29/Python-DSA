class Solution(object):
    def removeOuterParentheses(self, s):
       res=""
       balance=0
       for ch in s:

        if ch=="(":
            if balance>0:
                res+="("
            balance+=1
        else:
            balance-=1
            if balance>0:
                res+=")"
            
       return res

        