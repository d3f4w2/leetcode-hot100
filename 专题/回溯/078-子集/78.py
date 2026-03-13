from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrace(start:int, path):
            result.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrace(i+1, path)
                path.pop()
        backtrace(0, [])
        return result
    
s = Solution()
print(s.subsets([1, 2, 3]))