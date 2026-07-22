class Solution(object):
    def subsetsWithDup(self, nums):
        result=[]
        subset=[]
        nums.sort()
        def backtrack(index):
            result.append(subset[:])
            
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                #take
                subset.append(nums[i])
                backtrack(i+1)
                #undo
                subset.pop()
               
        backtrack(0)
        return result

    
        