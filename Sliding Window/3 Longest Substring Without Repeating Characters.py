class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        left = 0
        check = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in check:
                check.remove(s[left])
                left += 1
            check.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length