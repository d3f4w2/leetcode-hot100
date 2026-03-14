from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                cur = num
                cur_len = 1
                
                while cur + 1 in num_set:
                    cur += 1
                    cur_len += 1

                longest = max(longest, cur_len)

        return longest
    
nums = [100,4,200,1,3,2]
s = Solution()
print(s.longestConsecutive(nums))