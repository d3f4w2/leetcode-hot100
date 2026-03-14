from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        result = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(interval[1], result[-1][1])

            else:
                result.append(interval)

        return result
        
    
s = Solution()
print(s.merge([[1, 3], [2, 6], [7, 9]]))