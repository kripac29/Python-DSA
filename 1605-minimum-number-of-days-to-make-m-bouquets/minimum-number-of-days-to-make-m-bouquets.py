class Solution(object):
    def minDays(self, bloomDay, m, k):
        low=min(bloomDay)
        high=max(bloomDay)    #m is the current day,m   → Many bouquets needed, k   → k flowers per bouquet
        #Can I make m bouquets using k adjacent flowers by day mid?"


        
        ans=-1
        while low<=high:
            flowers=0
            bouqets=0

            mid=(low+high)//2
            for day in bloomDay:
                if day<=mid:
                    flowers+=1
                else:
                    flowers=0
                if flowers==k:
                    bouqets+=1
                    flowers=0
                    #so we are writing here bouqets >m that means bouqet 3 can be made on mid 5th day let's say then we will save 5th day and search for lesser or else higher 
            if bouqets>=m:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
            
                


        