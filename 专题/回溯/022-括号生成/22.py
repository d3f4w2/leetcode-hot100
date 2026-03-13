class Solution():
    def generateParenthesis(self, n):
        result = []
        def backtrace(path, left, right):
            if len(path) == 2 * n:
                result.append(path)
                return
            if left < n:
                backtrace(path + '(', left + 1, right)
            if right < left:
                backtrace(path + ')', left, right + 1)

        backtrace('', 0, 0)
        return result   
     
s = Solution()
print(s.generateParenthesis(3))

