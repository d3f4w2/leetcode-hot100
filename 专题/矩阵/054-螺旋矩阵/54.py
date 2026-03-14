def spiralOrder(matrix):
    if not matrix:
        return []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    result = []
    while left <= right and top <= bottom:
        for j in range(left, right+1):
            result.append(matrix[top][j])
        top += 1
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1
        for j in range(right, left-1, -1):
            result.append(matrix[bottom][j])
        bottom -= 1
        for i in range(bottom, top-1, -1):
            result.append(matrix[i][left])
        left += 1
    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))
