class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    def build(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = build(left, mid-1)
        root.right = build(mid+1, right)
        return root
    return build(0, len(nums)-1)

# 测试样例
nums = [1, 2, 3]
root = sortedArrayToBST(nums)

# 验证树的结构
def print_tree(node):
    if not node:
        return
    print(node.val)
    print_tree(node.left)
    print_tree(node.right)

print("前序遍历结果：")
print_tree(root)  # 输出: 2, 1, 3
