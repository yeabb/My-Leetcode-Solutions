class Solution:
      
    def countSubstrings(self, s: str) -> int:

        res=0
        for i in range(len(s)):
            
            #check for odd length of palindrom

            res+= self.countPalindrome(i, i, s)

            #check for even length of palindrom
            res+= self.countPalindrome(i, i+1, s)
        
            
           
        return res

    def countPalindrome(self, left, right, s):
        res=0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left-=1
            right+=1
            res+=1
        return res

    
        