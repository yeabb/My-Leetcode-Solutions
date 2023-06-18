import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
#If we use min heap algorithm for this problem, the runtime will be O(klogn)

        # heapq.heapify(nums)  #O(n)

        # while len(nums)>k:       #O(klogn) ****NB. for a large number n and small number k this is almost the same as O(n)*****
        #     heapq.heappop(nums)

        # return nums[0]

    #If we use a quickSelect algorithm the runtime will be O(n) on the average time but it will be O(n^2) on the worst case making the algorithm solution faster than the heap approach

        def quickSelect(l, r):
            p=l
            for i in range(l,r):
                if nums[i]<= nums[r]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p+=1
            nums[p], nums[r] = nums[r], nums[p]

            if k<p:
                return quickSelect(l, p-1)
            elif k>p:
                return quickSelect(p+1, r)
            else:
                return nums[p]
        k=len(nums)-k    
        return quickSelect(0, len(nums)-1)
        