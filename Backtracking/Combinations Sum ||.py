from collections import defaultdict
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backTracking(start, remain):
            if remain<0:
                return 
            elif remain==0:
                res.append(tempList.copy())
                return
            
            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                tempList.append(candidates[i])
                backTracking(i+1, remain-candidates[i])
                tempList.pop()
        
        candidates.sort()
        res=[]
        tempList=[]
        backTracking(0, target)
        return res

    
# nums=[10,1,2,7,6,1,5] ---> [1,1,2,5,6,7,10] 
#templist = [1,]
#used=[1:True, 2: False, 5: False, 6: False, 7: False, 10: False,]
#res = []