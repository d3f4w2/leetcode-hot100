from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        n = len(heights)
        max_area = 0
        stack = []
        for index, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                h = heights[stack.pop()]
                w = index if not stack else index - stack[-1] -1
                max_area = max(max_area, w * h)
            stack.append(index)
        return max_area


# --- 测试验证 ---
s = Solution()

# 测试用例 1
t1 = [2, 1, 5, 6, 2, 3]
print(f"输入: {t1}")
print(f"输出: {s.largestRectangleArea(t1)}") 
# 预期: 10 (5和6组成的矩形，宽2高5)
print("-" * 30)

# 测试用例 2 (全递增)
t2 = [1, 2, 3, 4, 5]
print(f"输入: {t2}")
print(f"输出: {s.largestRectangleArea(t2)}")
# 预期: 9 (3,4,5 组成宽3高3? 不对。
# 1x5=5, 2x4=8, 3x3=9, 4x2=8, 5x1=5 -> 最大是 9)
print("-" * 30)

# 测试用例 3 (全相同)
t3 = [2, 2, 2, 2]
print(f"输入: {t3}")
print(f"输出: {s.largestRectangleArea(t3)}")
# 预期: 8 (2x4)