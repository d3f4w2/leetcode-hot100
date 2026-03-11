from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n-2):

            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = n -1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-4,-1,-1,0,1,2]))