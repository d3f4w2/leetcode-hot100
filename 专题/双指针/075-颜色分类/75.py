from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        cur = 0
        right = len(nums) - 1
        while cur <= right:
            if nums[cur] == 1:
                cur += 1
            elif nums[cur] == 2:
                nums[right], nums[cur] = nums[cur], nums[right]
                right -= 1
            else:
                nums[left], nums[cur] = nums[cur], nums[left]
                cur += 1
                left += 1

s = Solution()
nums = [0,1,2,1,2,0,0]
s.sortColors(nums)
print(nums)