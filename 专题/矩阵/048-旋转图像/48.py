from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j] = matrix[j][i]
        for i in range(n):
            matrix[i].reverse()


matrix = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
s.rotate(matrix)
print(matrix)