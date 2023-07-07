class Solution:
    def rob(self, nums: List[int]) -> int:

        
        def houseRob(newNums):
            
            prev_prev_prev, prev_prev, prev = newNums[0], newNums[1], max(newNums[2]+newNums[0], newNums[1])

            for i in range(3, len(newNums)):
                curr = max(prev, newNums[i] + prev_prev, newNums[i] + prev_prev_prev)
                prev_prev_prev=prev_prev
                prev_prev=prev
                prev=curr
            return prev

        if len(nums)<=3:
            return max(nums)

        res1=houseRob(nums[1:])
        res2=houseRob(nums[:len(nums)-1])
        return max(res1, res2)
