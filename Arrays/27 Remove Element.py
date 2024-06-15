class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if len(nums) == 0:
            return 0

        start = 0
        end = len(nums)-1

        while(start < end):
            if nums[end] == val:
                end-=1
            else:
                if nums[start] == val:
                    temp = nums[start]
                    nums[start] = nums[end]
                    nums[end] = temp
                    end-=1
                start+=1

        if(nums[start] == val):       
            return start
        else:
            return start + 1