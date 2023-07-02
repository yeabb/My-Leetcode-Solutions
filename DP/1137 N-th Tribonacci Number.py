class Solution:
    def tribonacci(self, n: int) -> int:

        #Optimal substructure?      Yes
        
        #Overlapping substructures?   Yes
        
        #is it dynamic programing?  Yes
        
     
        #Bottom up (Tabulation) (Iterative)---------------------------------------------

        if n==0:
            return 0
        if 0 < n <= 2:
            return 1

        prev=1
        prev_prev=1
        prev_prev_prev=0
        for i in range(3, n+1):
            curr=prev + prev_prev + prev_prev_prev
            prev_prev_prev=prev_prev
            prev_prev=prev
            prev=curr
        return curr
            
            
       #Top down (Memoization) (Recursive)-------------------------------------------------

       
        # def dp(i):
        #     if i==0:
        #         return i
        #     if 0<i<=2:
        #         return 1
            
        #     if i not in memo:
        #         memo[i]=dp(i-1)+dp(i-2)+dp(i-3)
            
        #     return memo[i]
        
        # memo={}
        # memo[0], memo[1], memo[2] = 0, 1, 1
        # if n <= 2:
        #     return memo[n]
        # dp(n)
        # return memo[n]