# 155. 最小栈

## 所属专题

- 栈

## 题目描述

设计一个支持：

- `push`
- `pop`
- `top`
- `getMin`

操作，并且所有操作都能在 **常数时间 `O(1)`** 内完成的栈。

实现 `MinStack` 类：

- `MinStack()` 初始化堆栈对象
- `void push(int val)` 将元素 `val` 推入堆栈
- `void pop()` 删除堆栈顶部元素
- `int top()` 获取栈顶元素
- `int getMin()` 获取栈中的最小元素

## 示例

### 示例 1

```text
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]
```

解释：

```text
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // 返回 -3
minStack.pop();
minStack.top();    // 返回 0
minStack.getMin(); // 返回 -2
```

## 题意理解

这道题不是普通的“实现一个栈”。

难点在于：

- 普通栈的 `push`、`pop`、`top` 很容易做到 `O(1)`
- 但 `getMin()` 也要求是 `O(1)`

如果我们只用一个普通栈，
每次调用 `getMin()` 时再去把整个栈遍历一遍找最小值，
那时间复杂度就是：

`O(n)`

这显然不符合题目要求。

所以这道题的核心是：

**在栈元素不断入栈、出栈的过程中，如何始终快速知道当前最小值。**

## 最直接的想法：每次 `getMin()` 时遍历

最容易想到的方法是：

- 用一个普通栈保存所有元素
- 当调用 `getMin()` 时，遍历整个栈找最小值

这个思路实现起来不难，
但是最大的问题是：

- `push` 是 `O(1)`
- `pop` 是 `O(1)`
- `top` 是 `O(1)`
- `getMin` 却变成了 `O(n)`

题目明确要求所有操作都要是常数时间，
所以这种做法不行。

我们需要继续想：

**能不能在每次 `push` / `pop` 的时候，顺便把“当前最小值”也维护好？**

## 优化思路：主栈 + 辅助最小栈

这是这道题最经典的解法。

我们维护两个栈：

- `stack`：正常保存所有入栈元素
- `min_stack`：保存“到当前为止可能成为最小值的元素”

### 主栈做什么

主栈很简单，
就是正常存数据。

例如依次执行：

```text
push(-2), push(0), push(-3)
```

那么主栈里就是：

```text
[-2, 0, -3]
```

### 辅助栈做什么

辅助栈不需要把所有元素都存进去，
它只需要记录：

- 当前最小值
- 以及最小值变化的历史

也就是说：

- 如果新入栈元素比当前最小值还小，或者等于当前最小值，就把它压入 `min_stack`
- 如果弹出的元素刚好等于当前最小值，就把 `min_stack` 的栈顶也一起弹出

这样 `min_stack` 的栈顶，永远就是当前栈内最小值。

## 为什么这个思路成立

假设我们按顺序压入：

```text
-2, 0, -3
```

主栈变化：

```text
[-2]
[-2, 0]
[-2, 0, -3]
```

辅助栈变化：

```text
[-2]
[-2]
[-2, -3]
```

你会发现：

- `0` 不是新的最小值，所以不用进 `min_stack`
- `-3` 比当前最小值 `-2` 更小，所以需要进 `min_stack`

因此任何时刻：

```text
getMin() = min_stack[-1]
```

都能直接得到答案。

## 用示例手推一遍

还是看题目的例子：

```text
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
```

### 第 1 步：`push(-2)`

主栈：

```text
[-2]
```

辅助栈：

```text
[-2]
```

因为辅助栈原本为空，
所以 `-2` 一定是当前最小值。

### 第 2 步：`push(0)`

主栈：

```text
[-2, 0]
```

辅助栈：

```text
[-2]
```

因为 `0` 不比 `-2` 更小，
所以不进入辅助栈。

### 第 3 步：`push(-3)`

主栈：

```text
[-2, 0, -3]
```

辅助栈：

```text
[-2, -3]
```

因为 `-3` 比当前最小值 `-2` 更小，
所以它要进入辅助栈。

### 第 4 步：`getMin()`

直接看辅助栈栈顶：

```text
-3
```

所以返回 `-3`。

### 第 5 步：`pop()`

主栈弹出 `-3`。

由于被弹出的这个元素刚好等于辅助栈栈顶，
说明当前最小值也一起被移除了，
所以辅助栈也要弹出一次。

主栈变成：

```text
[-2, 0]
```

辅助栈变成：

```text
[-2]
```

### 第 6 步：`top()`

主栈栈顶是：

```text
0
```

所以返回 `0`。

### 第 7 步：`getMin()`

辅助栈栈顶现在是：

```text
-2
```

所以返回 `-2`。

## 为什么 `push` 时要写 `<=`

这是这道题最容易写错的地方之一。

代码里通常会写：

```python
if not self.min_stack or val <= self.min_stack[-1]:
    self.min_stack.append(val)
```

很多人会想：

```python
val < self.min_stack[-1]
```

是不是也行？

其实不行。

### 看一个例子

依次执行：

```text
push(-2)
push(-2)
pop()
getMin()
```

如果你在 `push` 时只写 `<`，
那么第二个 `-2` 不会进入辅助栈。

这时：

- 主栈是 `[-2, -2]`
- 辅助栈却只有 `[-2]`

接着执行一次 `pop()`，
主栈弹出一个 `-2`，
辅助栈也会弹出一个 `-2`。

结果变成：

- 主栈还有 `[-2]`
- 辅助栈却空了

但实际上当前最小值明明还是 `-2`。

所以为了正确处理“重复最小值”，
必须写成：

```python
val <= self.min_stack[-1]
```

## 为什么 `pop` 时要同步判断

`pop()` 也不能只弹主栈。

因为如果被弹出的元素刚好就是当前最小值，
那么辅助栈也必须一起更新。

所以标准写法是：

```python
if self.stack.pop() == self.min_stack[-1]:
    self.min_stack.pop()
```

它表示：

- 先弹出主栈栈顶
- 如果这个值正好等于当前最小值
- 就说明最小值被移除了
- 辅助栈也要同步弹出

## 算法步骤

1. 初始化两个空栈：`stack` 和 `min_stack`
2. `push(val)` 时，先把 `val` 压入 `stack`
3. 如果 `min_stack` 为空，或者 `val <= min_stack[-1]`，就把 `val` 也压入 `min_stack`
4. `pop()` 时，先弹出 `stack` 栈顶元素
5. 如果弹出的值等于 `min_stack[-1]`，就把 `min_stack` 也弹出
6. `top()` 直接返回 `stack[-1]`
7. `getMin()` 直接返回 `min_stack[-1]`

## 复杂度分析

### 时间复杂度

所有操作都是：

`O(1)`

因为：

- `push` 只做常数次比较和入栈
- `pop` 只做常数次比较和出栈
- `top` 直接访问栈顶
- `getMin` 直接访问辅助栈栈顶

### 空间复杂度

`O(n)`

因为最坏情况下，
比如元素单调递减：

```text
5, 4, 3, 2, 1
```

每个元素都会进入辅助栈，
所以额外空间是线性的。

## Python 参考实现（详细注释）

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # 只有当新元素不大于当前最小值时，
        # 才需要进入辅助栈。
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # 如果弹出的元素刚好就是当前最小值，
        # 说明辅助栈也需要同步弹出。
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

## 这段代码最值得记住的地方

这题你真正要记住的不是整段模板，
而是这条主线：

```python
self.stack.append(val)
if not self.min_stack or val <= self.min_stack[-1]:
    self.min_stack.append(val)

if self.stack.pop() == self.min_stack[-1]:
    self.min_stack.pop()
```

本质上就是一句话：

**主栈负责正常存数据，辅助栈负责记录“最小值出现的历史”，这样就能在任意时刻用 `O(1)` 得到当前最小值。**

## 常见错误

### 1. `getMin()` 时遍历整个栈

这样会让 `getMin()` 退化成：

`O(n)`

不符合题目要求。

### 2. `push` 时把判断写成 `<`

这样会丢失重复最小值的信息，
导致后续 `pop()` 后最小值错误。

正确写法必须是：

```python
val <= self.min_stack[-1]
```

### 3. `pop()` 时只弹主栈，不更新辅助栈

如果被删除的是当前最小值，
那 `min_stack` 也必须同步更新，
否则 `getMin()` 就会返回错误结果。

### 4. 把辅助栈理解成“存所有元素”

辅助栈不是另一个完全复制的主栈，
它的作用是：

- 只维护最小值变化历史
- 让我们可以在 `O(1)` 时间拿到当前最小值

## 适合自己默写的精简版本

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

## 一句话总结

这道题的关键是：

**用一个普通栈存所有元素，再用一个辅助栈同步维护最小值变化历史，这样 `push`、`pop`、`top`、`getMin` 都能保持 `O(1)`。**
