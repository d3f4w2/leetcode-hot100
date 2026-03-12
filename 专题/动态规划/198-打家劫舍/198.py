from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        pre2 = nums[0]
        pre1 = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            cur_max = max(pre1, pre2+nums[i])
            pre2 = pre1
            pre1 = cur_max
        return cur_max
    
s = Solution()
print(s.rob([2,1,3,4,5,6]))