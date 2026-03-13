from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result



# --- 3. 测试代码 ---
if __name__ == "__main__":
    # 手动构建一颗简单的二叉树:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    # 创建节点
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2 = TreeNode(2, node4, node5)  # 节点2的左是4，右是5
    node3 = TreeNode(3)                # 节点3没有孩子
    root = TreeNode(1, node2, node3)   # 根节点1，左是2，右是3

    # 调用函数
    sol = Solution()
    res = sol.levelOrder(root)
    
    # 打印结果
    print("层序遍历结果:", res)
