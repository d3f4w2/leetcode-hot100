class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        def expand(left:int, right:int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left -1
        for i in range(len(s)):
            cur_len = max(expand(i,i), expand(i, i+1))
            if cur_len > end - start:
                start = i - (cur_len - 1)//2
                end = i + cur_len//2
        return s[start:end+1]

    
s = Solution()
print(s.longestPalindrome('alabba'))
print(s.longestPalindrome('cabad'))