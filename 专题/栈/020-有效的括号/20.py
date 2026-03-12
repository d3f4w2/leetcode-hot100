class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for char in s:
            if char in map:
                if not stack or stack.pop() != map[char]:
                    return False
            else:
                stack.append(char)
        return not stack

    
s = Solution()
print(s.isValid('(){}'))
print(s.isValid('()'))
print(s.isValid('([)])'))