class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        charCount = {}
        for chr in s:
            if chr in charCount:
                charCount[chr] +=1
            else:
                charCount[chr] = 1

        for chr in t:
            if chr not in charCount or charCount[chr] <= 0:
                return False
            charCount[chr] -= 1

        return True

