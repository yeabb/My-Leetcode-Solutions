class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backTracking(remain, start):
            if remain<0:
                return
            elif remain==0:
                res.append(tempList.copy())
                return
            

            for i in range(start, len(candidates)):
                tempList.append(candidates[i])
                backTracking(remain-candidates[i], i)
                tempList.pop()
        res=[]
        tempList=[]
        backTracking(target, 0)
        return res