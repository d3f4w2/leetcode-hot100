from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        now = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(now):
                now = now[:-1]
            if not now:
                return ''
        return now
    
# --- 测试代码 ---
solver = Solution()

# 样例 1: 正常情况，有公共前缀
test1 = ["flower", "flow", "flight"]
print(f"输入: {test1}")
print(f"输出: '{solver.longestCommonPrefix(test1)}'") 
# 预期: "fl"

# 样例 2: 没有公共前缀
test2 = ["dog", "racecar", "car"]
print(f"\n输入: {test2}")
print(f"输出: '{solver.longestCommonPrefix(test2)}'") 
# 预期: "" (空字符串)