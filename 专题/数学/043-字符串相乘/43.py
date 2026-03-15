class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        for i in range(m-1, -1, -1):
            digit1 = int(num1[i])
            for j in range(n-1, -1, -1):
                digit2 = int(num2[j])
                mul = digit1 * digit2
                p2 = i + j + 1
                p1 = i + j
                total = mul + result[p2]
                result[p2] = total % 10
                result[p1] += total //10

        start = 0
        while start < len(result) and result[start] == 0:
            start += 1
        return ''.join(str(digit) for digit in result[start:])

# --- 测试执行 ---
solver = Solution()
print(solver.multiply('123', '456'))
