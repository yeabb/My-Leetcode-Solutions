class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
    #we use binary search
    #after we find the target in nums, we still have to look for left and right bounds
    
    
    #call the helper function
        l=self.binSearch(nums,target,True)
        r=self.binSearch(nums,target,False)
        return([l,r])
    
    
    #Helper function
    def binSearch(self,nums, target, leftBound):
        left,right=0,len(nums)-1
        i=-1
        
        while(left<=right):
            mid=left+(right-left)//2
            
            if(target>nums[mid]):
                left=mid+1
            elif(target<nums[mid]):
                right=mid-1
            else:
                i=mid
                
                if leftBound:
                    right=mid-1
                else:
                    left=mid+1
        return i

