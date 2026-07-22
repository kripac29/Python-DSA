class Solution(object):
    def partition(self, s):
        result=[]
        path=[]
        
        def backtrack(index):
            #basecase 
            if index==len(s):
                result.append(path[:])
                return
            for i in range(index,len(s)):
                part=s[index:i+1] #part is the current substring that we are considering
                 #now if the current substring is plaindrome or not wee check 
                if part==part[::-1]:
                    #choose
                    path.append(part)
                    backtrack(i+1)
                    path.pop()
        backtrack(0)
        return result
