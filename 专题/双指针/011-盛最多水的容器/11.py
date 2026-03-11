from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 左指针从最左边开始，右指针从最右边开始。
        left = 0
        right = len(height) - 1
        best  = 0
        while left < right :
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            best = max(best, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))