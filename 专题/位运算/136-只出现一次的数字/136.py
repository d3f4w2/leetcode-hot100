from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
s = Solution()
print(s.singleNumber([1,2,2,3,3]))