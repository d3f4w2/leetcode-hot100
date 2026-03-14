from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i < m and j >= 0:
            if target == matrix[i][j]:
                return True
            if target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False

            



matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]
target = 5

s = Solution()

print(s.searchMatrix(matrix, target))