from typing import List
def singleNumber(self, nums: List[int]) -> int:
    resultado = 0
    for num in nums:
        resultado ^= num
    return print(resultado)
nums = [1,2,3,3,1,4]
singleNumber(0, nums)