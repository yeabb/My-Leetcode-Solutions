class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backTracking():
            if len(perms)==len(nums):
                res.append(perms.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i]=True
                    perms.append(nums[i])
                    backTracking()
                    used[i]=False
                    perms.pop()
                    
        res=[]
        perms=[]
        used=[False]*len(nums)
        backTracking()
        return res    