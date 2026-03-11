from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
            n = len(nums)
            i = n - 2
            while nums[i] >= nums[i + 1] and i >= 0:
                  i -= 1

            if i >= 0:
                j = n - 1
                while nums[j] <= nums[i] and j > i:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                left = i + 1
                right = n - 1
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
s = Solution()
nums = [1,2,3,7,3,2,1]
s.nextPermutation(nums)
print(nums)