class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPolindrome(left, right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        def backTracking(start):
            if start==len(s):
                res.append(subset.copy())
                return


            for i in range(start, len(s)):
                if isPolindrome(start,i):
                    subset.append(s[start:i+1])
                    backTracking(i+1)
                    subset.pop()
        res=[]
        subset=[]
        backTracking(0)
        return res