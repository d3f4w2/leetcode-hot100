class Solution:
    def isSymmetric(self, root) -> bool:
        def ismirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return(
                left.val == right.val
                and ismirror(left.left, right.right)
                and ismirror(left.right, right.left)
            )
        if not root:
            return True
        return ismirror(root.left, root.right)
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 构造对称二叉树
#       1
#      / \
#     2   2
#    / \ / \
#   3  4 4  3
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))

print(Solution().isSymmetric(root))  # True
