# 094. 二叉树的中序遍历

## 所属专题

- 二叉树

## 题目描述

给定一个二叉树的根节点 `root`，返回它的 **中序遍历** 结果。

所谓中序遍历，顺序就是：

- 先遍历左子树
- 再访问当前节点
- 最后遍历右子树

也就是常说的：

```text
左 -> 根 -> 右
```

## 示例

### 示例 1

```text
输入：root = [1,null,2,3]
输出：[1,3,2]
解释：
- 根节点是 1
- 1 没有左子树
- 1 的右子节点是 2
- 2 的左子节点是 3

按照中序遍历顺序：
先访问 1，再访问 3，最后访问 2，所以结果是 [1,3,2]
```

### 示例 2

```text
输入：root = []
输出：[]
```

### 示例 3

```text
输入：root = [1]
输出：[1]
```

## 题意理解

这道题不是让我们修改二叉树，
也不是让我们求什么路径、深度或者节点个数。

它只要求我们做一件事：

- 按照中序遍历的顺序，把所有节点值依次收集起来

关键在于，你必须牢牢记住中序遍历的访问顺序：

```text
左子树 -> 当前节点 -> 右子树
```

例如一棵树如果是：

```text
    1
     \
      2
     /
    3
```

那么中序遍历不是：

- `1,2,3`

而是要注意：

- 右子树里的左孩子，要先于右子树根节点被访问

更准确地说：

1. 先看 `1` 的左子树，没有
2. 所以访问 `1`
3. 再去看 `1` 的右子树，也就是以 `2` 为根的子树
4. 对节点 `2` 来说，要先访问它的左子树 `3`
5. 然后访问 `2`

最终顺序就是：

- `[1,3,2]`

## 最直接的想法：递归

这道题最自然的想法就是递归。

为什么？

因为二叉树本身就是递归结构：

- 一个节点有左子树
- 一个节点有右子树
- 左子树和右子树本身又都是二叉树

所以我们完全可以直接按照中序遍历的定义来写：

1. 递归遍历左子树
2. 把当前节点值加入结果数组
3. 递归遍历右子树

也就是说，思路几乎就是把“中序遍历”的定义原封不动地翻译成代码。

如果当前节点是空节点，
那就什么都不做，直接返回。

这个方法非常直观，
也是很多人写二叉树遍历时最先掌握的写法。

## 优化思路：迭代 + 栈

虽然递归很好写，
但很多时候面试官会继续问：

- 能不能不用递归？

这时候就要用：

- 栈

来模拟递归过程。

### 核心思想

递归在系统底层，本质上也是在用“调用栈”保存状态。

所以如果我们手动准备一个栈，
也能完成同样的事情。

中序遍历的关键是：

- 一路先往左走
- 直到走不动为止
- 然后回到最近的那个还没访问过的节点
- 访问它
- 再转向它的右子树

所以迭代写法通常是这样：

1. 准备一个栈 `stack`
2. 准备一个指针 `curr` 指向当前节点
3. 当 `curr` 不为空时，就不断把它和它的左孩子压栈
4. 当左边走到底后，弹出栈顶节点并访问
5. 然后把 `curr` 指向这个节点的右孩子
6. 重复上述过程

### 为什么一定要“先一路向左”

因为中序遍历要求：

- 左边处理完了，才能访问当前节点

所以我们必须先把一条路径上的所有左节点都记下来。

而栈顶保存的，正是“最近那个左边已经处理完、但自己还没访问的节点”。

## 用示例手推一遍

以示例 1 为例：

```text
root = [1,null,2,3]
```

对应的树结构是：

```text
    1
     \
      2
     /
    3
```

下面用迭代写法手推一遍，最容易看懂整个过程。

### 初始状态

- `curr = 1`
- `stack = []`
- `result = []`

### 第 1 步：一路向左

当前 `curr = 1`

- 把 `1` 入栈
- 然后让 `curr = 1.left`

因为 `1.left = None`，所以现在：

```text
stack = [1]
curr = None
```

### 第 2 步：左边走到底，弹栈访问

现在 `curr` 为空，说明左边走不动了。

弹出栈顶节点 `1`：

- 访问 `1`，结果变成 `[1]`
- 然后转向 `1.right`

此时：

```text
stack = []
curr = 2
result = [1]
```

### 第 3 步：继续一路向左

当前 `curr = 2`

- 先把 `2` 入栈
- 再让 `curr = 2.left = 3`

接着 `curr = 3`

- 把 `3` 入栈
- 再让 `curr = 3.left = None`

此时：

```text
stack = [2, 3]
curr = None
result = [1]
```

### 第 4 步：访问节点 3

弹出栈顶节点 `3`：

- 访问 `3`
- `result = [1,3]`
- 然后转向 `3.right`

因为 `3.right = None`，所以：

```text
stack = [2]
curr = None
result = [1,3]
```

### 第 5 步：访问节点 2

再次弹出栈顶节点 `2`：

- 访问 `2`
- `result = [1,3,2]`
- 然后转向 `2.right`

因为 `2.right = None`，所以：

```text
stack = []
curr = None
result = [1,3,2]
```

### 结束

现在：

- `curr = None`
- `stack = []`

循环结束。

最终答案就是：

```text
[1,3,2]
```

## 为什么这样写

### 1. 中序遍历的定义就是“左、根、右”

这道题不是技巧题，
核心首先是记住遍历顺序。

只要顺序写错，
就会把中序遍历写成：

- 前序遍历：根 -> 左 -> 右
- 后序遍历：左 -> 右 -> 根

所以最重要的第一步不是背代码，
而是先把“访问时机”理解清楚。

### 2. 递归写法是在直接翻译定义

递归版最自然的地方就在于：

- 先处理左边
- 再处理自己
- 最后处理右边

这和题目要求完全一致。

### 3. 迭代写法里，栈保存的是“还没访问值的节点”

这些节点有一个共同特点：

- 它们自己还没被加入答案
- 但它们的左边正在被处理，或者马上要被处理

一旦左边处理完，
就轮到栈顶节点被访问。

### 4. 弹栈后一定要去右子树

这是迭代写法里最容易漏掉的一步。

因为一个节点被访问之后，
按照中序顺序，下一步应该去处理：

- 它的右子树

所以必须写：

```python
curr = curr.right
```

## 算法步骤

### 递归版

1. 创建结果数组 `result`
2. 定义递归函数 `inorder(node)`
3. 如果 `node` 为空，直接返回
4. 递归遍历 `node.left`
5. 把 `node.val` 加入 `result`
6. 递归遍历 `node.right`
7. 从根节点开始调用递归函数
8. 返回 `result`

### 迭代版

1. 创建结果数组 `result`
2. 创建栈 `stack`
3. 用指针 `curr` 指向根节点
4. 只要 `curr` 不为空，就不断入栈并向左移动
5. 当左边走到底时，弹出栈顶节点并访问
6. 然后把 `curr` 指向该节点的右孩子
7. 重复直到 `curr` 为空并且栈也为空
8. 返回 `result`

## 复杂度分析

### 时间复杂度

`O(n)`

其中：

- `n` 是二叉树中的节点总数

原因：

- 每个节点都会被访问恰好一次

### 空间复杂度

`O(h)`

其中：

- `h` 是二叉树的高度

原因：

- 递归版使用的是递归调用栈
- 迭代版使用的是显式栈
- 在最坏情况下（树退化成链表），空间复杂度会达到 `O(n)`

## Python 参考实现（详细注释）

### 写法一：递归

```python
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 用来保存最终的中序遍历结果。
        result = []

        def inorder(node: Optional[TreeNode]) -> None:
            # 如果当前节点为空，说明这条分支已经走到底了，直接返回。
            if not node:
                return

            # 第一步：先递归遍历左子树。
            inorder(node.left)

            # 第二步：左子树处理完后，再访问当前节点。
            result.append(node.val)

            # 第三步：最后递归遍历右子树。
            inorder(node.right)

        # 从根节点开始做中序遍历。
        inorder(root)

        # 返回完整结果。
        return result
```

### 写法二：迭代（栈）

```python
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 保存答案。
        result = []

        # 手动维护一个栈，用来模拟递归调用过程。
        stack = []

        # curr 表示当前正在处理的节点。
        curr = root

        # 只要当前节点还存在，或者栈里还有待处理节点，就继续循环。
        while curr or stack:
            # 一路向左走，把路径上的节点都压栈。
            # 这样才能保证最左边的节点最先被访问。
            while curr:
                stack.append(curr)
                curr = curr.left

            # 走到这里，说明左边已经走到底。
            # 弹出最近一个“左边处理完但自己还没访问”的节点。
            curr = stack.pop()

            # 访问这个节点。
            result.append(curr.val)

            # 按照中序遍历规则，接下来应该去它的右子树。
            curr = curr.right

        return result
```

## 这段代码最值得记住的地方

如果你先记递归版，
最核心的是这三步顺序：

```python
inorder(node.left)
result.append(node.val)
inorder(node.right)
```

也就是：

- 左
- 根
- 右

如果你想练非递归版，
最需要记住的是这个模板：

```python
while curr or stack:
    while curr:
        stack.append(curr)
        curr = curr.left

    curr = stack.pop()
    result.append(curr.val)
    curr = curr.right
```

这段模板的本质就是：

- 先一路向左
- 左边走完再访问当前节点
- 访问完再去右边

## 常见错误

### 1. 把中序遍历顺序写错

很多人会不小心写成：

- 前序：根 -> 左 -> 右

或者：

- 后序：左 -> 右 -> 根

而正确的中序必须是：

- 左 -> 根 -> 右

### 2. 递归里把 `append` 放错位置

例如如果你写成：

```python
result.append(node.val)
inorder(node.left)
inorder(node.right)
```

那就变成前序遍历了。

### 3. 迭代写法里弹栈后忘了转向右子树

如果少了这句：

```python
curr = curr.right
```

那后面的右子树就不会被遍历到。

### 4. 空树时没有正确返回空数组

如果 `root = []`，
答案应该是：

```text
[]
```

而不是报错，
也不是返回 `None`。

## 适合你自己再写一遍的版本

如果你准备先默写一个最稳定的版本，
建议先记递归写法：

```python
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result
```

如果你还想顺手练一下非递归，
也可以再默写这一版：

```python
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        return result
```

## 一句话总结

这道题的关键不是“把树走一遍”这么简单，而是：

**牢牢记住中序遍历的访问顺序是 `左 -> 根 -> 右`，递归是直接翻译定义，迭代则是用栈手动模拟这个过程。**
