from typing import List

def containsDuplicate(self, nums: List[int]) -> bool:
    hashmap = set()
    for i in nums:
        if i in hashmap: 
            return print(True)
        hashmap.add(i)
    return print(False) 
        
    
nums = [1,3,2,1]
containsDuplicate(0, nums)