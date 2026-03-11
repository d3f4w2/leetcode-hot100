from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        for i in range(1,n):
            answer[i] = answer[i-1] * nums[i-1]
        right = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        return answer



s = Solution()
print(s.productExceptSelf([1,2,3,4]))