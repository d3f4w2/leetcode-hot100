from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 先排序，把相同元素放到一起，方便后面去重。
        nums.sort()

        # 保存最终结果。
        result = []

        def backtrack(start: int, path: List[int]) -> None:
            result.append(path.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return result
    
s = Solution()
print(s.subsetsWithDup([1, 2, 2]))