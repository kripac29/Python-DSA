class Solution(object):
    def singleNumber(self, nums):
        xor=0
        for num in nums:
            xor=xor^num
        return xor
        

        
        
        