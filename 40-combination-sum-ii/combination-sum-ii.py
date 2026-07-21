class Solution(object):
    def combinationSum2(self, candidates, target):
        result=[]
        subset=[]
        candidates.sort()
        def backtrack(index,currentsum):
            if currentsum==target:
                result.append(subset[:])
                return
            for i in range(index, len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                if currentsum+candidates[i]>target:
                    break
                #takeeee
                subset.append(candidates[i])
                backtrack(i+1,currentsum+candidates[i])
                #undo
                subset.pop()
        backtrack(0,0)
        return result
            
        
        