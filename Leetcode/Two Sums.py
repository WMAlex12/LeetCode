from typing import List

class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in hashmap: 
                
                return [hashmap[diff], i]
            hashmap[n] = i   
            print(hashmap, i)
        return        
        

    nums = [0,3,2,5]
    target = 7
    twoSum( nums, target)

