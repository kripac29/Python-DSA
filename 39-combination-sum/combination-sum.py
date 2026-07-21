class Solution(object):
    def combinationSum(self, candidates, target):
        result=[]
        subset=[]
        def backtrack(index,currentsum):
            if currentsum==target:
                result.append(subset[:])
                return
            if index==len(candidates) or currentsum>target:

                return
            #take
            subset.append(candidates[index])
            backtrack(index,currentsum+candidates[index])
            #undo
            subset.pop()
            #don't take
            backtrack(index+1,currentsum)
        backtrack(0,0)
        return result

        
        