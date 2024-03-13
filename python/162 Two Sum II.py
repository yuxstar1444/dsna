#Brute force, start with index 0, iterate through entire array, O(n^2)
# 2 Pointer: array is sorted, we can use this advantage

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l ,r = 0, len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target: 
                l+= 1
            else: 
                return [l+1, r+1]
        return []

        