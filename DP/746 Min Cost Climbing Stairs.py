
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
   
        
        #Optimal substructure?      Yes
        
        #Overlapping substructures?   Yes
        
        #is it dynamic programing?  Yes
        
        
        #Bottom up (Tabulation) (Iterative)---------------------------------------------
        
        
           
        # if(len(cost)<=2):
        #     return min(cost)
        
        
        # prev=cost[1]
        # prev_prev=cost[0]
        # for i in range(2, len(cost)):
            
        #     curr=min(prev, prev_prev)
            
        #     prev_prev=prev
        #     prev=curr+cost[i]
            
        # return(min(prev, prev_prev))
         

        def dp(i):
            if i<2:
                return cost[i]
            if i not in memo:
                if i<len(cost):
                    memo[i]=cost[i]+min(dp(i-1), dp(i-2))
                else:
                    memo[i]=min(dp(i-1), dp(i-2))
            return memo[i]
        
        if len(cost)<=2:
            return min(cost)
        memo={}
        memo[0]=cost[0]
        memo[1]=cost[1]
        minCost=dp(len(cost))
        return minCost
        