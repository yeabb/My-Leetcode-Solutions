class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
#         output=[[]]
#         for i in nums:
#             output+=[lst+[i] for lst in output]
#         return output
    
    #other way of writing the above code is
    
        # output=[[]]
        # for i in nums:
        #     for j in range(len(output)):
        #         output.append(output[j]+[i])

        # return output

    #another way of solving this with backtracking
        
        def backTracking(start):
            res.append(subset.copy())
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backTracking(i+1)
                subset.pop()
        res=[]
        subset=[]
        backTracking(0)
        return res

