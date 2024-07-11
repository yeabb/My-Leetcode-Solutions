class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        hashSet = set(nums)
        length = 1
        maxLength = 1
        for num in nums:
            if num - 1 not in hashSet:
                currNum = num + 1
                while currNum in hashSet:
                    length += 1
                    currNum += 1

                maxLength = max(length, maxLength)
                length = 1

        return maxLength





    