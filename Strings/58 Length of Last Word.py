class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        #Solution 1 ( Better runtime because we don't have to process the whole string s in best cases)
        count = 0
        for i in range(len(s)-1, -1, -1):
            j = i
            while (j>=0 and s[j] != " "):
                count+=1
                j-=1
            if count > 0:
                return count
            
            
        #Solution 2 (Slightly slower because we have to process the whole string s when spliting)
        return len(s.split()[-1])