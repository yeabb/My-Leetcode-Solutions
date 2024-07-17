class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Solution 1 -------------------------------------
        lowestPrice = prices[0]
        output = 0

        for i in range(1, len(prices)):
            lowestPrice = min(lowestPrice, prices[i])
            output = max(output, prices[i]-lowestPrice)
            
        return output
    
    
        #Solution 2 --------------------------------------
        
        # left=0
        # right=1
        # profit=0
        # while(right<len(prices)):
            
        #     if prices[left]>prices[right]:
        #         left=right
        #     else:
        #         tempProf=prices[right]-prices[left]
        #         profit=max(tempProf, profit)
        #     right+=1
            
        # return profit