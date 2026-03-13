from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        def backtrace(path:List[int]) -> None:
            if len(path) == len(nums):
                result.append(path.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrace(path)
                path.pop()
                used[i] = False
        backtrace([])
        return result

    
s = Solution()
print(s.permute([1, 2, 3]))