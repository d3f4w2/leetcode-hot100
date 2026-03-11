from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        for index, num in enumerate(nums):
            if nums[index] > 0:
                result.append(index + 1)
        return result
    
s = Solution()
print(s.findDisappearedNumbers([1,3,5,3,6,3]))