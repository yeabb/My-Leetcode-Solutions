class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        # ****** Note the difference between substring and subsequence *********
        
        # We can convert this problem to Longest Common Subsequence, then use DP

        #Using DP --------------------------------------------
        
        s2 = s[::-1]
        m = len(s)
        n = len(s2)

        dp=[[0] * (m+1) for _ in range(n+1)]

        for col in range(m-1, -1, -1):
            for row in range(n-1, -1, -1):
                if s[col] == s2[row]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])
        
        return dp[0][0]
        

    
        
       