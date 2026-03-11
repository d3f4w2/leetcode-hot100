from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], index]
            seen[num] = index
        return []

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))