from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        if not nums: 
            return 0 
        for i in range(1, len(nums)):
            if(nums[i]!=nums[k]): 
               k += 1 
               nums[k] = nums[i]
               
        
        # for i in range(k + 1, len(nums)):
        #         nums[i] = "_"

        return k + 1
    
solution = Solution()
nums = [0,0,0,1,1,2,3,3,3,4,4,5,6,6]
result = solution.removeDuplicates(nums)
print(result)
print(nums) 
