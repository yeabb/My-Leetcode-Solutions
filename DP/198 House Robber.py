class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #Optimal substructure?      Yes
        
        #Overlapping substrcures?   Yes
        
        #is it dynamic programing?  Yes
      

#Bottom up (Tabulation) (Iterative)--------------------------------------
        
        if len(nums)<=2:
            return max(nums)
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=nums[1]
        
        for i in range(2, len(nums)):
            if(i-3)<0:
                dp[i]=nums[i]+dp[i-2]
            else:
                dp[i]=nums[i]+max(dp[i-2], dp[i-3])
        return max(dp)
        
        
#Top down (Memoization) (Recursive)--------------------------------------
        
        
#         def dp(i):
#             #base case
#             if(i<=1):
#                 return nums[i]
#             if(i not in dic):
#                 if (i-3<0):
#                     dic[i]=nums[i]+dic[i-2]
#                 else:
#                     dic[i]=nums[i]+max(dp(i-2), dp(i-3))
#             return dic[i]
        
#         if(len(nums)<=2):
#             return max(nums)
#         dic={}
#         dic[0]=nums[0]
#         dic[1]=nums[1]
        
#         n=len(nums)
#         for i in range(2):
#             dp(n-i-1)
#         return max(dic.values())
