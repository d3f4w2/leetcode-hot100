from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, index):
            if board[i][j] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            tmp = board[i][j]
            board[i][j] = '#'

            dir = [(-1, 0), (1, 0), (0, 1),(0, -1)]

            for dx, dy in dir:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    if dfs(ni, nj, index+1):
                        board[i][j] = tmp
                        return True
                    
            board[i][j] = tmp
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
                
        return False
    
if __name__ == "__main__":
    sol = Solution()

    # --- 测试用例 1: 能够找到单词 ---
    board1 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word1 = "ABCCED"
    # 预期输出: True
    # 解释: 路径是 (0,0)A -> (0,1)B -> (0,2)C -> (1,2)C -> (2,2)E -> (2,1)D
    print(f"输入 board1, word='{word1}'")
    print(f"输出: {sol.exist(board1, word1)}")
    print("-" * 20)

    # --- 测试用例 2: 无法找到单词 ---
    board2 = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word2 = "ABCB"
    # 预期输出: False
    # 解释: A -> B -> C 之后，右边的 C 已访问，下边的 S 不匹配，左边越界，上边越界，无路可走。
    print(f"输入 board2, word='{word2}'")
    print(f"输出: {sol.exist(board2, word2)}")
