from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            
            def find_first(nums:List[int], target:int) -> int:
                  
                  left, right = 0, len(nums)
                  while left < right:
                        mid = (left + right) // 2
                        if nums[mid] < target:
                              left = mid + 1
                        else:
                              right = mid
                  if left < len(nums) and nums[left] == target:
                        return left
                  else:
                        return -1
            

            def find_last(nums:List[int], target:int) -> int:
                  left, right = 0, len(nums)
                  while left < right:
                        mid = (left + right) // 2
                        if nums[mid] <= target:
                              left = mid + 1
                        else:
                              right = mid
                  if left < len(nums) and nums[left - 1] == target:
                        return left - 1
                  else:
                        return -1

            first = find_first(nums, target)
            if first == -1:
                  return [-1, -1]
            last = find_last(nums, target)
            return [first, last]
s = Solution()
print(s.searchRange([1,2,2,2,3], 2))
