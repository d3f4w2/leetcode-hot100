from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        water = 0
        left_max = 0
        right_max = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1
            
        return water



# --- 测试驱动代码 ---
s = Solution()

def test_case(name, input_data, expected):
    result = s.trap(input_data)
    status = "✅ 通过" if result == expected else f"❌ 失败 (得到 {result})"
    print(f"{name}: {status}")
    if result != expected:
        print(f"   输入: {input_data}")
        print(f"   预期: {expected}, 实际: {result}")
    print("-" * 40)

# 1. 经典案例 (LeetCode 官方示例)
# 图示:
#       #
#   #   ##
# # # # ###
# 012345678
# 索引 2 处积水 1, 索引 4 处积水 1, 索引 5 处积水 2, 索引 6 处积水 1 (不对，重新算)
# 正确推导:
# [0,1,0,2,1,0,1,3,2,1,2,1]
# 积水分布:
# idx 2 (高0): min(1, 3)-0 = 1
# idx 4 (高1): min(2, 3)-1 = 1
# idx 5 (高0): min(2, 3)-0 = 2
# idx 6 (高1): min(2, 3)-1 = 1
# idx 9 (高1): min(3, 2)-1 = 1 (右边最大值是2) -> 等等，右边最大值在变化
# 标准答案是 6
test_case("经典案例", [0,1,0,2,1,0,1,3,2,1,2,1], 6)

# 2. 空数组
test_case("空数组", [], 0)

# 3. 只有一个柱子 (无法积水)
test_case("单柱子", [5], 0)

# 4. 两个柱子 (无论多高，无法积水)
test_case("双柱子", [3, 5], 0)
test_case("双柱子逆序", [5, 3], 0)

# 5. 单调递增 (水流走，无积水)
test_case("单调递增", [1, 2, 3, 4, 5], 0)

# 6. 单调递减 (水流走，无积水)
test_case("单调递减", [5, 4, 3, 2, 1], 0)

# 7. 凹字形 (标准水桶)
# 5 0 0 0 5 -> 中间3个格子，每个深5，共15
test_case("完美凹字", [5, 0, 0, 0, 5], 15)

# 8. 凸字形 (无积水)
test_case("凸字形", [1, 3, 1], 0)

# 9. 多个山峰 (复杂情况)
# [3, 0, 2, 0, 4]
# idx 1 (0): min(3, 4)-0 = 3
# idx 2 (2): min(3, 4)-2 = 1 (左边最大3，右边最大4，当前2) -> 实际上这里不会积水吗？
# 让我们手动模拟双指针:
# L=0(3), R=4(4). L_max=3, R_max=4. L<R -> 处理L. water+=0. L->1
# L=1(0), R=4(4). L_max=3, R_max=4. L<R -> 处理L. water+=3-0=3. L->2
# L=2(2), R=4(4). L_max=3, R_max=4. L<R -> 处理L. water+=3-2=1. L->3
# L=3(0), R=4(4). L_max=3, R_max=4. L<R -> 处理L. water+=3-0=3. L->4
# Total = 3+1+3 = 7.
test_case("多山峰", [3, 0, 2, 0, 4], 7)

# 10. 全为0
test_case("全零", [0, 0, 0, 0], 0)

# 11. 只有两边高中间低，但中间有起伏
# [4, 2, 0, 3, 2, 5]
# 预期计算:
# idx 1 (2): min(4, 5)-2 = 2
# idx 2 (0): min(4, 5)-0 = 4
# idx 3 (3): min(4, 5)-3 = 1
# idx 4 (2): min(4, 5)-2 = 2
# Total = 2+4+1+2 = 9
test_case("中间起伏", [4, 2, 0, 3, 2, 5], 9)

print("所有测试完成！")