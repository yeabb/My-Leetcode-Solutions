class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        summ=nums[0]+nums[1]+nums[2]
        
        for i in range(0,len(nums)-1):
            
            if(i>0 and nums[i]==nums[i-1]):
                continue
                
            l,r=i+1,len(nums)-1
            
            while(l<r):
                
                sumNow=nums[i]+nums[l]+nums[r]
                
                if(abs(target-summ)>abs(target-sumNow)):
                    summ=sumNow
                else:
                    pass
                
                if(sumNow>target):
                    r-=1
                else:
                    l+=1
                    
                
        return summ
    
    #Run time= O(n^2)
    #Number of times solved this problem-- Once
        