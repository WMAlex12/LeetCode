from typing import List 

class Solution:
    def rotate(self, nums: List[int], k: int):
        if not nums or k == 0: 
            return nums 
        
        #Ajustar rotaciones 
        n = len(nums)
        k = k % n
        
        # Realizar la rotación en-place usando espacio de memoria constante
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        # Paso 1: Invertir toda la matriz
        reverse(nums, 0, n - 1)

        # Paso 2: Invertir las primeras k elementos
        reverse(nums, 0, k - 1)

        # Paso 3: Invertir los elementos restantes después de k
        reverse(nums, k, n - 1)

solution = Solution()
entrada = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution.rotate(entrada, k)
print("Matriz Rotada:", entrada)
