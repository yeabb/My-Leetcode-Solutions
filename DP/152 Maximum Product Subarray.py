class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        minProd, maxProd = 1, 1
        res = max(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                minProd, maxProd = 0, 0
                
            else:
                tempMin = minProd
                minProd = min(nums[i], nums[i] * tempMin, nums[i] * maxProd) 
                maxProd = max(nums[i], nums[i] * maxProd, nums[i] * tempMin) 
            res = max(res, maxProd)
        
        return res
