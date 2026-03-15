from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre = stack.pop()
                answer[pre] = i - pre
            stack.append(i)
        return answer
    
# --- 测试样例 ---
s = Solution()

t1 = [73, 74, 75, 71, 69, 72, 76, 73]
print(f"输入: {t1}")
print(f"输出: {s.dailyTemperatures(t1)}")
print(f"预期: [1, 1, 4, 2, 1, 1, 0, 0]")
print("-" * 30)

t2 = [80, 70, 60, 50]
print(f"输入: {t2}")
print(f"输出: {s.dailyTemperatures(t2)}")
print(f"预期: [0, 0, 0, 0]")
print("-" * 30)