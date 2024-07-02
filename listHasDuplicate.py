from typing import List
# ? Given an integer array nums, return true if any value 
# appears more than once in the array, otherwise return false.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            j = i
            while nums[j - 1] > nums[j] and j > 0:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                j -= 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i + 1]:
                return True
        return False
nums = [4, 3, 7, 8, 2,1]
solution = Solution()
print(solution.hasDuplicate(nums))