from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        
        dp=[]
        dic=defaultdict(int)
        for x in nums:
            if x not in dic:
                dp.append(x)
            dic[x]+=1
        dp.sort()
        
        prev, prev_prev = 0, 0
        for i in range(len(dp)):
            curr = dp[i] * dic[dp[i]]
            if i > 0 and dp[i-1]==dp[i]-1:
                temp=prev
                prev=max(prev, curr+prev_prev)
                prev_prev=temp
            else:
                temp=prev
                prev=curr + prev
                prev_prev=temp

        return prev
                
        

            
            
        