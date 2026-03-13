# 101. 对称二叉树

## 所属专题

- 二叉树

## 题目描述

给你一个二叉树的根节点 `root`，检查它是否轴对称。

也就是说，判断这棵树是否关于根节点所在的中轴线左右镜像。

## 示例

### 示例 1

```text
输入：root = [1,2,2,3,4,4,3]
输出：true
```

### 示例 2

```text
输入：root = [1,2,2,null,3,null,3]
输出：false
```

## 题意理解

这道题不是在问：

- 左子树和右子树是否完全相同

而是在问：

- 左子树和右子树是否互为镜像

“镜像”的意思是：

- 左边的左孩子，要和右边的右孩子对应
- 左边的右孩子，要和右边的左孩子对应

例如这棵树：

```text
        1
      /   \
     2     2
    / \   / \
   3   4 4   3
```

它就是对称的。

因为：

- 左边最外侧的 `3` 和右边最外侧的 `3` 对应
- 左边内侧的 `4` 和右边内侧的 `4` 对应

但是如果结构或数值有任意一处对不上，
就不是对称二叉树。

## 最直接的想法：同时比较左右两棵子树

这道题最自然的想法就是：

- 不要单独看某一边
- 而是把左子树和右子树放在一起比较

如果它们是镜像关系，
那么必须同时满足三件事：

1. 两个节点的值相等
2. 左子树的左孩子和右子树的右孩子镜像对称
3. 左子树的右孩子和右子树的左孩子镜像对称

你会发现这个条件本身就带着“递归结构”：

- 要判断两棵树是否镜像
- 需要继续判断它们的子树是否镜像

所以这题非常适合用递归。

## 优化思路：递归判断两棵树是否镜像

我们定义一个辅助函数：

```text
isMirror(left, right)
```

它表示：

- 判断 `left` 和 `right` 这两棵树是否互为镜像

### 递归终止条件

#### 情况 1：两个节点都为空

```text
left is None and right is None
```

说明这两个位置完全对应，
所以返回：

```text
True
```

#### 情况 2：一个为空，一个不为空

说明结构已经不对称，
直接返回：

```text
False
```

#### 情况 3：两个节点都不为空，但值不同

说明数值不对称，
也要返回：

```text
False
```

### 递归向下比较

如果前面的基本条件都通过了，
那么还要继续检查：

- `left.left` 和 `right.right` 是否镜像
- `left.right` 和 `right.left` 是否镜像

所以递归公式就是：

```text
isMirror(left, right) =
    left.val == right.val
    and isMirror(left.left, right.right)
    and isMirror(left.right, right.left)
```

最后主函数只需要判断：

- 根节点的左子树
- 和根节点的右子树

是否镜像即可。

## 用示例手推一遍

以：

```text
root = [1,2,2,3,4,4,3]
```

为例。

对应的树是：

```text
        1
      /   \
     2     2
    / \   / \
   3   4 4   3
```

### 第 1 步：比较根节点两侧

调用：

```text
isMirror(root.left, root.right)
```

也就是比较：

- 左边的 `2`
- 右边的 `2`

它们值相同，继续往下。

### 第 2 步：比较外侧

调用：

```text
isMirror(left.left, right.right)
```

也就是比较：

- 左边的 `3`
- 右边的 `3`

值相同，继续检查它们的子节点。

由于它们下面都是空节点，
所以这一支返回 `True`。

### 第 3 步：比较内侧

调用：

```text
isMirror(left.right, right.left)
```

也就是比较：

- 左边的 `4`
- 右边的 `4`

同样值相同，下面也都为空，
所以这一支也返回 `True`。

### 第 4 步：汇总结果

外侧对称，内侧也对称，
因此整棵树返回：

```text
True
```

## 再看一个不对称的例子

```text
root = [1,2,2,null,3,null,3]
```

对应结构大致是：

```text
        1
      /   \
     2     2
      \     \
       3     3
```

这里的问题在于：

- 左子树的 `3` 在右边
- 右子树的 `3` 也在右边

如果是镜像，
它们应该一个在右边、一个在左边。

也就是说：

- 结构不对称

所以答案是：

```text
False
```

## 为什么这样写

### 1. “对称”本质上就是“镜像”

很多人第一次做这题时，
会想成：

- 左子树等于右子树

但其实不是“相同”，
而是“镜像”。

所以比较方式必须是交叉比较：

- 左左 对 右右
- 左右 对 右左

### 2. 递归天然适合处理树的镜像结构

树的问题里，
只要你发现：

- 当前节点的问题，依赖子树的同类问题

那递归通常就是非常自然的写法。

这题刚好符合：

- 判断当前两棵树是否镜像
- 依赖它们更小的子树是否镜像

### 3. 不仅要值相等，还要结构对称

有些例子节点值看起来一样，
但如果空节点的位置不对，
仍然不能算对称。

所以：

- 结构
- 数值

这两方面都必须同时满足。

## 算法步骤

1. 如果根节点为空，直接返回 `True`
2. 定义递归函数 `isMirror(left, right)`
3. 如果 `left` 和 `right` 都为空，返回 `True`
4. 如果只有一个为空，返回 `False`
5. 如果两个节点值不同，返回 `False`
6. 递归比较 `left.left` 和 `right.right`
7. 递归比较 `left.right` 和 `right.left`
8. 两边都为 `True` 时，当前才返回 `True`
9. 主函数返回 `isMirror(root.left, root.right)`

## 复杂度分析

### 时间复杂度

`O(n)`

其中 `n` 是二叉树的节点数。

原因是：

- 每个节点最多被访问一次

### 空间复杂度

`O(h)`

其中 `h` 是二叉树的高度。

原因是：

- 递归调用栈的深度最多等于树高

如果树退化成链表，
最坏情况下空间复杂度会变成：

```text
O(n)
```

## Python 参考实现（详细注释）

```python
class Solution:
    def isSymmetric(self, root) -> bool:
        def isMirror(left, right):
            # 两个节点都为空，说明这一对位置是对称的
            if not left and not right:
                return True

            # 一个为空，一个不为空，结构不对称
            if not left or not right:
                return False

            # 当前节点值必须相同，
            # 并且外侧子树、内侧子树都要镜像对称
            return (
                left.val == right.val
                and isMirror(left.left, right.right)
                and isMirror(left.right, right.left)
            )

        if not root:
            return True

        return isMirror(root.left, root.right)
```

## 这段代码最值得记住的地方

你在自己手写的时候，
最值得记住的其实就是这一句：

```python
isMirror(left.left, right.right) and isMirror(left.right, right.left)
```

它正好体现了“镜像比较”的本质：

- 外侧对外侧
- 内侧对内侧

只要把这个关系真正想明白，
这题就很容易写出来。

## 常见错误

### 1. 把“镜像”写成“相同”

错误思路通常会去比较：

- `left.left` 和 `right.left`
- `left.right` 和 `right.right`

这其实是在判断两棵树是否相同，
不是在判断它们是否镜像。

### 2. 只比较节点值，不比较空节点结构

树的对称不仅看数值，
还要看结构。

如果某一边有节点、另一边没有，
即使别的位置值都一样，
也不是对称树。

### 3. 忘记处理空树

空树本身也是对称的，
所以：

```python
if not root:
    return True
```

这一句不要漏掉。

### 4. 递归终止条件写不全

最容易漏的是：

- 两个都空时返回 `True`
- 一个空一个不空时返回 `False`

这两个基础判断一定要先写清楚。

## 适合你自己再写一遍的版本

如果你准备在 `.ipy` 文件里默写，
可以先记住下面这个精简版：

```python
class Solution:
    def isSymmetric(self, root) -> bool:
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (
                left.val == right.val
                and isMirror(left.left, right.right)
                and isMirror(left.right, right.left)
            )

        if not root:
            return True

        return isMirror(root.left, root.right)
```

## 一句话总结

这道题的关键不是判断左右子树是否相同，而是：

**判断左右子树是否互为镜像，也就是递归比较“左的左”和“右的右”、“左的右”和“右的左”。**
