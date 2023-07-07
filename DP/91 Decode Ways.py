from collections import defaultdict
class Solution:
    def numDecodings(self, s: str) -> int:


        #Iteratively---------------------------------

        
        prev = 1
        prev_prev = 1

        for i in range(len(s)-1, -1, -1):

            if s[i] == "0":
                temp = 0
            else:
                temp = prev
            
            if i+2 <= len(s) and (s[i] == "1" or (s[i] == "2" and 0 <= int(s[i+1]) < 7)):
                temp+= prev_prev

            prev_prev = prev    
            prev = temp
            
        return prev




        #Recursive -----------------------------------
        
        """
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            count = dfs(i+1)

            if i+2 <= len(s) and (s[i] == "1" or (s[i] == "2" and 0 <= int(s[i+1]) < 7)):
                count+=dfs(i+2)
        
            dp[i] = count
            return dp[i]

        dp=defaultdict(int)
        dp[len(s)] = 1
        return dfs(0)

        """
        