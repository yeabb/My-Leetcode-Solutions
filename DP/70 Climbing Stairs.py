class Solution:
    def climbStairs(self, n: int) -> int:
        
        #Iterative ------------------------------------

        # Base cases
        prev_prev = 0
        prev = 1

        for i in range(n):
            temp=prev
            prev = prev + prev_prev
            prev_prev=temp
        
        return prev

     #Recursive -------------------------------------------

        # def dp(i):
        #     if i==0:
        #         return 1
        #     if i==1:
        #         return 2

        #     if i not in dic:
        #         dic[i]=dp(i-1)+dp(i-2)
        #     return dic[i]
        # dic={}
        # return dp(n-1)