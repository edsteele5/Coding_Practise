class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=0
        
        test2=0
        test2 = sum(nums[:k])
        test = test2
        
        
        n = len(nums)
        
        while j+k<n:
            
           
            test =  test + nums[j+k] - nums[j]
            
            if test > test2:
                test2 = test
            j = j + 1
            i = j
       
            
        avr = test2 / k
        return avr
        