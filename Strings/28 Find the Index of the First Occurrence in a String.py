class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for i in range(len(haystack)):
            needleTracker = 0
            haystackTracker = i
            while ((needleTracker < len(needle) and haystackTracker < len(haystack) ) and (needle[needleTracker] == haystack[haystackTracker])):
                needleTracker+=1
                haystackTracker+=1
            if needleTracker == len(needle):
                return i
        return -1

        
#Runtime = O(n X m) such that n = len(needle), m = len(haystack)