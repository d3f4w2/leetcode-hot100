import unittest
from typing import Optional

# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre = None
        def inorder(node:Optional[TreeNode]) -> bool:
            nonlocal pre
            if not node:
                return True
            if not inorder(node.left):
                return False
            if pre is not None and pre >= node.val:
                return False
            pre = node.val
            return inorder(node.right)
        return inorder(root)

class TestIsValidBST(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_tree(self):
        """空树应该是合法的 BST"""
        self.assertTrue(self.sol.isValidBST(None))

    def test_single_node(self):
        """单节点树应该是合法的 BST"""
        root = TreeNode(1)
        self.assertTrue(self.sol.isValidBST(root))

    def test_valid_bst_simple(self):
        """简单的合法 BST: [2, 1, 3]"""
        #   2
        #  / \
        # 1   3
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertTrue(self.sol.isValidBST(root))

    def test_invalid_bst_right_smaller(self):
        """非法 BST: 右子节点比根小 [1, 2, 3] (结构: 1->right=2, 2->right=3 是合法的，但这里构造非法结构)
           构造: 
             3
            / \
           2   1  <-- 1 < 3, 非法
        """
        root = TreeNode(3, TreeNode(2), TreeNode(1))
        self.assertFalse(self.sol.isValidBST(root))

    def test_invalid_bst_left_larger(self):
        """非法 BST: 左子节点比根大
           构造:
             1
            / \
           3   2  <-- 3 > 1, 非法
        """
        root = TreeNode(1, TreeNode(3), TreeNode(2))
        self.assertFalse(self.sol.isValidBST(root))

    def test_duplicate_values(self):
        """包含重复值应该返回 False (严格递增)
           构造:
             2
            / \
           1   2  <-- 右边的 2 不大于 prev (2)，非法
        """
        root = TreeNode(2, TreeNode(1), TreeNode(2))
        self.assertFalse(self.sol.isValidBST(root))
        
    def test_duplicate_in_left(self):
        """左子树包含重复值
           构造:
             2
            / \
           2   3  <-- 左边的 2 不小于 prev (无)，但在访问根节点 2 时，prev 已经是 2 了 (来自左子树最右节点)
           实际中序遍历: 2 (左) -> 2 (根). 2 <= 2, 非法
        """
        # 构造一个左子树最右节点等于根节点的情况
        #   2
        #  /
        # 1
        #  \
        #   2
        root = TreeNode(2)
        root.left = TreeNode(1, None, TreeNode(2))
        self.assertFalse(self.sol.isValidBST(root))

    def test_complex_invalid_deep(self):
        """深层嵌套的非法情况 (经典陷阱)
           构造:
               5
              / \
             1   6
                / \
               4   7  <-- 4 < 5, 虽然在 6 的左边，但也必须大于 5。非法。
           
           中序遍历序列应为: 1, 5, 4, 6, 7
           当访问到 4 时，prev 是 5。4 <= 5，应返回 False。
        """
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(6, TreeNode(4), TreeNode(7))
        self.assertFalse(self.sol.isValidBST(root))

    def test_large_valid_bst(self):
        """较大的合法 BST"""
        #       10
        #      /  \
        #     5    15
        #    / \   / \
        #   1   7 12  20
        root = TreeNode(10)
        root.left = TreeNode(5, TreeNode(1), TreeNode(7))
        root.right = TreeNode(15, TreeNode(12), TreeNode(20))
        self.assertTrue(self.sol.isValidBST(root))

if __name__ == '__main__':
    unittest.main()