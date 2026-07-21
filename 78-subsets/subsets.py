class Solution(object):
    def subsets(self, nums):
        result=[]
        subset=[]
        def backtrack(index):
            if index==len(nums):
                result.append(subset[:])
                return
            #take
            subset.append(nums[index])
            backtrack(index+1)
            #pop
            subset.pop()
            #don't take
            backtrack(index+1)
        backtrack(0)
        return result


       
        