class Solution(object):
    def romanToInt(self, s):
        value={
            
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans=0 
        prev=0
        for ch in s[::-1]:
            if value[ch]<prev:
                ans-=value[ch]
            else:
                ans+=value[ch]
            prev=value[ch]
        return ans
        

        
        