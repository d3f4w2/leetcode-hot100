from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(nums[i], nums[i]+cur_sum)
            max_sum = max(cur_sum, max_sum)
        return max_sum
    
s = Solution()
print(s.maxSubArray([1,2,3,4,-1,-2,4]))