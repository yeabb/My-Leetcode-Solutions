class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        arrForward = [1]
        arrBackward = [1]
        
        backTracker = -1
        for i in range(0, len(nums)-1):
            arrForward.append(arrForward[i] * nums[i])
            arrBackward.append(arrBackward[i] * nums[backTracker])
            backTracker-=1

        arrBackward = arrBackward[::-1]
        output = []

        for i in range(len(nums)):
            output.append(arrForward[i] * arrBackward[i])
        return output 

