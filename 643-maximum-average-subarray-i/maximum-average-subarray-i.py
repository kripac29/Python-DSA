class Solution(object):
    def findMaxAverage(self, nums, k):
        n=len(nums)
        total=sum(nums[:k])
        maxi=total
        for i in range(k,n):
            total=total+nums[i]-nums[i-k]
            maxi=max(maxi,total)
        return float(maxi)/k

      
        