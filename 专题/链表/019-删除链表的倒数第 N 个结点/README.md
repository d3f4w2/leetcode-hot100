# 019. 删除链表的倒数第 N 个结点

## 所属专题
- 链表

## 题目描述

给你一个链表的头节点 `head`，删除链表的倒数第 `n` 个结点，并返回链表的头节点。

## 示例

### 示例 1

```text
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
```

### 示例 2

```text
输入：head = [1], n = 1
输出：[]
```

### 示例 3

```text
输入：head = [1,2], n = 1
输出：[1]
```

## 题意理解

这道题的目标不是“找到倒数第 `n` 个节点的值”，而是：

- 真的把这个节点从链表里删掉
- 并返回删除后的新链表头节点

链表和数组不一样。

数组可以直接通过下标访问：

- 第 1 个
- 第 2 个
- 倒数第 1 个
- 倒数第 2 个

但单链表只能从前往后走，
不能直接从尾部往前找。

所以这道题的关键在于：

- 如何在只遍历一遍链表的情况下
- 找到“倒数第 `n` 个节点”的前一个节点

因为真正删除一个节点时，常见写法并不是“删当前节点本身”，
而是：

```python
prev.next = prev.next.next
```

也就是说，
我们最需要找到的是：

- **倒数第 `n` 个节点的前一个节点**

## 最直接的想法：先算长度，再删除

最容易想到的方法是分两步：

1. 先遍历一遍链表，求出链表长度 `length`
2. 倒数第 `n` 个节点，就是正数第 `length - n + 1` 个节点
3. 再遍历一遍，走到它的前一个节点，完成删除

这个思路完全可以做出来，
而且逻辑也不难。

但是它有一个问题：

- 需要遍历链表两次

虽然时间复杂度仍然是 `O(n)`，
但这道题更经典的解法是：

- **双指针一次遍历完成**

## 优化思路：双指针 + 虚拟头节点

### 核心想法

定义两个指针：

- `fast`
- `slow`

让 `fast` 先走 `n + 1` 步，
这样 `fast` 和 `slow` 之间就会保持一个固定间距。

然后再让它们一起向前移动：

- 当 `fast` 走到 `None` 时
- `slow` 正好停在“倒数第 `n` 个节点的前一个节点”

此时直接执行：

```python
slow.next = slow.next.next
```

就可以删掉目标节点。

### 为什么要用虚拟头节点 `dummy`

这道题里，最容易出问题的边界情况就是：

- 要删除的刚好是头节点

例如：

```text
head = [1], n = 1
```

或者：

```text
head = [1,2,3], n = 3
```

如果没有虚拟头节点，
你就要专门判断：

- 当前删的是不是头节点
- 删除后新的头节点该是谁

这样代码会变得零碎。

如果加一个 `dummy` 放在头节点前面：

```text
dummy -> head -> ...
```

那么无论删除的是：

- 头节点
- 中间节点
- 尾节点

都可以统一写成：

```python
slow.next = slow.next.next
```

最后返回：

```python
dummy.next
```

即可。

### 为什么 `fast` 要先走 `n + 1` 步

因为我们要让 `slow` 最后停在：

- 目标删除节点的前一个位置

如果 `fast` 只先走 `n` 步，
最后 `slow` 停到的位置会不好统一处理。

而让 `fast` 从 `dummy` 出发先走 `n + 1` 步后：

- `fast` 和 `slow` 的间隔就是 `n + 1`
- 当 `fast` 走到空时
- `slow.next` 恰好就是倒数第 `n` 个节点

这时删除就非常自然。

## 用示例手推一遍

以示例 1 为例：

```text
head = [1,2,3,4,5], n = 2
```

我们想删除的是：

- 倒数第 2 个节点，也就是值为 `4` 的节点

加上虚拟头节点后：

```text
dummy -> 1 -> 2 -> 3 -> 4 -> 5
```

初始时：

- `slow = dummy`
- `fast = dummy`

### 第一步：`fast` 先走 `n + 1 = 3` 步

走完后：

- `slow` 还在 `dummy`
- `fast` 在值为 `3` 的节点

### 第二步：`fast` 和 `slow` 一起走

一起移动：

1. `fast` 到 `4`，`slow` 到 `1`
2. `fast` 到 `5`，`slow` 到 `2`
3. `fast` 到 `None`，`slow` 到 `3`

此时：

- `slow` 正好停在值为 `3` 的节点
- `slow.next` 就是值为 `4` 的节点

执行删除：

```python
slow.next = slow.next.next
```

链表变成：

```text
1 -> 2 -> 3 -> 5
```

返回结果：

```text
[1,2,3,5]
```

## 为什么这样写

### 1. 单链表删除节点，本质上是改前一个节点的 `next`

你不能直接“跳到目标节点后删掉它”，
因为删除操作真正改的是：

- 前一个节点的指针

所以我们一定要想办法找到：

- 目标节点的前驱节点

### 2. 双指针能把“倒数”转成“同步前进”

“倒数第 `n` 个”听起来像是要从后往前数，
但链表不支持倒着走。

双指针的巧妙之处就在于：

- 先制造一个固定距离
- 再同步前进
- 最后自然定位到目标前驱

这是一类非常经典的链表技巧。

### 3. `dummy` 能统一处理删除头节点的情况

很多链表题里，
只要涉及“删除节点”，
虚拟头节点几乎都是值得优先考虑的技巧。

因为它可以把：

- “删除头节点”
- “删除普通节点”

统一成同一种写法。

### 4. 整个过程只需要一次遍历

`fast` 先走一段，
之后两个指针一起走。

虽然表面上像分了两部分，
但整体仍然只是在链表上线性前进，
所以时间复杂度仍然是：

- `O(n)`

## 算法步骤

1. 创建虚拟头节点 `dummy`，让 `dummy.next = head`
2. 定义两个指针 `fast`、`slow`，都从 `dummy` 出发
3. 先让 `fast` 向前走 `n + 1` 步
4. 然后让 `fast` 和 `slow` 同时向前走
5. 当 `fast` 走到空时，`slow` 正好在目标节点前一个位置
6. 执行 `slow.next = slow.next.next` 删除节点
7. 返回 `dummy.next`

## 复杂度分析

### 时间复杂度

`O(n)`

原因是：

- `fast` 和 `slow` 都只是在链表上向前走
- 每个节点最多被访问常数次

### 空间复杂度

`O(1)`

原因是：

- 只使用了几个指针变量
- 没有使用和链表长度相关的额外空间

## Python 参考实现（详细注释）

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # 先让 fast 走 n + 1 步
        for _ in range(n + 1):
            fast = fast.next

        # fast 和 slow 一起移动
        while fast:
            fast = fast.next
            slow = slow.next

        # 删除倒数第 n 个节点
        slow.next = slow.next.next

        return dummy.next
```

## 常见错误

### 1. 不使用 `dummy`，导致删除头节点时单独写很多判断

例如当：

- `head = [1]`
- `n = 1`

这时删除的就是头节点。

如果没有 `dummy`，
代码很容易变乱。

### 2. `fast` 先走的步数写错

这题最常见的细节错误之一就是：

- 不小心写成走 `n` 步
- 或者循环边界写错

如果你采用的是“从 `dummy` 出发”的写法，
那就记住：

- `fast` 先走 `n + 1` 步

### 3. 最后删错节点

真正删除操作应该是：

```python
slow.next = slow.next.next
```

因为 `slow` 停在的是：

- 目标节点的前一个节点

### 4. 忘记返回 `dummy.next`

尤其在删除头节点时，
新的头节点可能已经不是原来的 `head` 了。

所以最终应该返回：

```python
dummy.next
```

## 适合自己默写的精简版本

```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
```

## 一句话总结

这道题的关键是：

**用虚拟头节点统一边界，再让快指针先走 `n + 1` 步，这样慢指针最终就会停在倒数第 `n` 个节点的前一个位置。**
