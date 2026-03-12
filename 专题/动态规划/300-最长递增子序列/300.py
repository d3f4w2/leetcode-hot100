class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
    
s = Solution()
print(s.lengthOfLIS([1,2,1,1,3,4,5]))