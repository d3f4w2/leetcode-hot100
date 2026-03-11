from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

s = Solution()
nums = [0,1,2,0,6]
s.moveZeroes(nums)
print(nums)