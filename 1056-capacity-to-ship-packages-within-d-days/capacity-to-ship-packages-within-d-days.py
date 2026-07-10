class Solution(object):
    def shipWithinDays(self, weights, days):
      
        low=max(weights)
        high=sum(weights)
        ans=-1
        
        while low<=high:
            mid=(low+high)//2
            daysused=1
            loadweight=0 #loadweight is capacity
            for weight in weights:
                if loadweight+weight<=mid:
                    #mid is the capacity here
                    loadweight+=weight
                else:
                    daysused+=1
                    loadweight=weight
            if daysused<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans

            
        
        