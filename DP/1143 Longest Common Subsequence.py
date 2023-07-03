from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:  

        #Iterative Solutiom --------------------------------------

        dp=[[0] * (len(text2)+1) for _ in range(len(text1)+1)]
    
        for col in range(len(text2)-1, -1 , -1):
            for row in range(len(text1)-1, -1, -1):
                if text1[row]==text2[col]:
                    dp[row][col]=1+dp[row+1][col+1]
                else:
                    dp[row][col]=max(dp[row+1][col], dp[row][col+1])
        return dp[0][0]




        #Recursive soluton ------------------------------------------

        # @lru_cache(maxsize=None)
        # def lcs(p1, p2):

        #     if p1==len(text1) or p2==len(text2):
        #         return 0

        #     #case1 --- when the line is not part of the solution
        #     if text1[p1] == text2[p2]:
        #         return 1 + lcs(p1+1, p2+1)

        #     #case2 ---- when the line part of the solution
        #     return max(lcs(p1+1, p2), lcs(p1, p2+1))
        
        # return lcs(0,0)

            
            