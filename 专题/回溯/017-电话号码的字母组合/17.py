from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        def backtrack(index:int, path:str) -> None:
            if index == len(digits):
                result.append(path)
                return
            letters = mapping[digits[index]]
            for letter in letters:
                backtrack(index+1, path + letter)
        
        backtrack(0, '')

        return result

if __name__ == "__main__":
    sol = Solution()

    # --- 测试用例 1: 正常输入 ---
    input_digits = "23"
    # 预期输出: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    # 解释:
    # 数字 '2' 对应 "abc"
    # 数字 '3' 对应 "def"
    # 组合为 a+d, a+e, a+f, b+d ...
    output = sol.letterCombinations(input_digits)
    print(f"输入: {input_digits}")
    print(f"输出: {output}")
    print("-" * 20)

    # --- 测试用例 2: 空输入 ---
    input_digits_empty = ""
    # 预期输出: []
    # 解释: 题目要求如果输入为空，返回空列表
    output_empty = sol.letterCombinations(input_digits_empty)
    print(f"输入: '{input_digits_empty}'")
    print(f"输出: {output_empty}")
