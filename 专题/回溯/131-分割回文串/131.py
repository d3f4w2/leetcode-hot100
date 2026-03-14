def partition(s):
    result = []
    def is_wen(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    def backtrace(start, path):
        if start == len(s):
            result.append(path.copy())
            return
        for end in range(start, len(s)):
            if is_wen(start, end):
                path.append(s[start:end+1])
                backtrace(end+1, path)
                path.pop()
    
    backtrace(0, [])
    return result

print(partition('aab'))