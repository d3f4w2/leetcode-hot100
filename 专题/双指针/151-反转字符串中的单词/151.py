from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        vaild_len = self.remove_extra_spaces(chars)
        chars = chars[:vaild_len]
        if not chars:
            return ''
        self.reverse(chars, 0, len(chars)-1)
        start = 0
        for end in range(len(chars)+1):
            if end == len(chars) or chars[end] == ' ':
                self.reverse(chars, start, end-1)
                start = end + 1

        return ''.join(chars)
    def remove_extra_spaces(self, chars: List[str]) -> int:
        fast = 0
        slow = 0
        n = len(chars)
        while fast < n and chars[fast] == ' ':
            fast += 1
        while fast < n:
            if chars[fast] != '':
                chars[slow] = chars[fast]
                slow += 1
            else:
                if slow > 0  and chars[slow - 1] != ' ':
                    chars[slow] = chars[fast]
                    slow += 1
            fast += 1
        if slow > 0 and chars[slow - 1] == ' ':
            slow -= 1
        return slow

    def reverse(self, chars: List[str], left: int, right: int) -> None:
        # 用双指针原地反转区间 [left, right]。
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

# --- 测试执行 ---
solver = Solution()

test_cases = [
    # 1. 标准情况：前后有空格，中间有多余空格
    "  hello world  ",
    
    # 2. 多个连续空格
    "a good   example",
    
    # 3. 单个单词（带空格）
    "  single  ",
    
    # 4. 全是空格
    "     ",
    
    # 5. 没有空格
    "hello",
    
    # 6. 空字符串
    "",
    
    # 7. 只有前导或尾随空格
    "   abc",
    "abc   "
]

for i, case in enumerate(test_cases, 1):
    result = solver.reverseWords(case)
    # 使用 repr() 可以清晰看到结果中的空格和引号
    print(f"测试 {i}: 输入 {repr(case)}")
    print(f"       输出 {repr(result)}")
    print("-" * 30)