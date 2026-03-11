# 033. 搜索旋转排序数组

## 所属专题
- 二分查找

## 题目描述

整数数组 `nums` 按升序排列，数组中的值 **互不相同**。

在传递给函数之前，`nums` 在预先未知的某个下标 `k`（`0 <= k < nums.length`）上进行了 **旋转**，
使数组变为：

```text
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
```

例如：

```text
[0,1,2,4,5,6,7]
```

在下标 `3` 处旋转后，可能变为：

```text
[4,5,6,7,0,1,2]
```

给你旋转后的数组 `nums` 和一个整数 `target`，
如果 `nums` 中存在这个目标值 `target`，则返回它的下标，否则返回 `-1`。

## 示例

### 示例 1

```text
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
```

### 示例 2

```text
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
```

### 示例 3

```text
输入：nums = [1], target = 0
输出：-1
```

## 题意理解

这道题乍一看像普通二分查找，
但麻烦在于：

- 原数组本来是升序的
- 但中间某个位置被旋转了
- 旋转后，整体看起来不再是完全有序

比如：

- 原数组：`[0,1,2,4,5,6,7]`
- 旋转后：`[4,5,6,7,0,1,2]`

虽然整个数组不再整体有序，
但它并不是“完全乱掉了”，而是：

**由两段有序数组拼接而成。**

题目还给了两个非常关键的信息：

- 数组中的值 **互不相同**
- 希望你尽量做到 `O(log n)`

这两点几乎就在提示我们：

**要用二分查找，而且要利用“旋转数组至少有一半仍然有序”这个性质。**

## 最直接的想法：从头到尾线性查找

最容易想到的方法是：

- 从左到右遍历整个数组
- 看每个位置是不是 `target`
- 找到就返回下标
- 找不到就返回 `-1`

这种方法当然能做出来，
而且逻辑很简单。

但问题在于：

- 最坏情况下要把整个数组看一遍
- 时间复杂度是 `O(n)`

而题目明显希望我们利用“有序”的信息，
把复杂度压到 `O(log n)`。

## 优化思路：二分查找

### 核心突破口

普通二分查找的前提是：

- 整个数组有序

但这道题里，整个数组虽然不是完全有序，
可每次取中点 `mid` 之后，

**`[left, mid]` 和 `[mid, right]` 这两半里，至少有一半一定是有序的。**

这是因为数组只是“旋转”了一次，
不是被打乱。

### 怎么判断哪一半有序

设：

- `left` 是左边界
- `right` 是右边界
- `mid = (left + right) // 2`

如果：

```python
nums[left] <= nums[mid]
```

说明：

- 左半部分 `[left, mid]` 是有序的

否则说明：

- 右半部分 `[mid, right]` 是有序的

这里之所以可以这样判断，
很重要的前提就是：

- **数组元素互不相同**

### 左半部分有序时怎么做

如果左半部分有序，
我们就判断 `target` 是否落在这个有序区间里：

```python
nums[left] <= target < nums[mid]
```

如果在：

- 说明答案一定在左边
- 让 `right = mid - 1`

如果不在：

- 说明答案只能去右边找
- 让 `left = mid + 1`

### 右半部分有序时怎么做

如果右半部分有序，
就判断 `target` 是否落在右边这个有序区间里：

```python
nums[mid] < target <= nums[right]
```

如果在：

- 说明答案在右边
- 让 `left = mid + 1`

如果不在：

- 说明答案去左边找
- 让 `right = mid - 1`

### 整个过程在做什么

本质上还是二分：

- 先看中点是不是答案
- 如果不是，就先判断哪一半有序
- 再判断 `target` 是否可能落在那一半有序区间中
- 从而舍弃掉另一半

也就是说，
每一次循环都能砍掉一半搜索空间，
所以复杂度仍然是 `O(log n)`。

## 用示例手推一遍

以：

```text
nums = [4,5,6,7,0,1,2], target = 0
```

为例。

初始时：

- `left = 0`
- `right = 6`

### 第 1 轮

- `mid = (0 + 6) // 2 = 3`
- `nums[mid] = 7`

先判断：

- `nums[mid]` 不是 `target`

再看哪一半有序：

- `nums[left] = 4`
- `nums[mid] = 7`
- 因为 `4 <= 7`
- 所以左半部分 `[4,5,6,7]` 有序

接着判断 `target = 0` 是否在左半部分范围内：

- `4 <= 0 < 7` 不成立

说明：

- `target` 不在左边
- 去右边找

更新：

- `left = mid + 1 = 4`

### 第 2 轮

- `left = 4`
- `right = 6`
- `mid = (4 + 6) // 2 = 5`
- `nums[mid] = 1`

先判断：

- `nums[mid]` 不是 `target`

再看哪一半有序：

- `nums[left] = 0`
- `nums[mid] = 1`
- 因为 `0 <= 1`
- 所以左半部分 `[0,1]` 有序

接着判断 `target = 0` 是否在左半部分范围内：

- `0 <= 0 < 1` 成立

说明答案在左边。

更新：

- `right = mid - 1 = 4`

### 第 3 轮

- `left = 4`
- `right = 4`
- `mid = 4`
- `nums[mid] = 0`

此时：

- `nums[mid] == target`

直接返回：

```text
4
```

## 为什么这样写

### 1. 虽然整体不完全有序，但至少有一半是有序的

这就是这道题还能继续用二分的根本原因。

如果每次都能确认一半有序，
就能继续判断 `target` 应该往哪边走。

### 2. 不能把它当成普通二分直接比较大小

普通二分里：

- `target < nums[mid]` 往左走
- `target > nums[mid]` 往右走

这道题不能这么简单处理，
因为数组整体不再是完整升序。

必须先判断：

- 哪一半有序

再利用这个有序区间去缩小范围。

### 3. “元素互不相同”这个条件很重要

因为没有重复元素时：

- `nums[left] <= nums[mid]`

就能比较清楚地判断左半部分是否有序。

如果允许重复元素，
情况会更复杂，那就是另一道题了。

### 4. 区间判断里的等号位置不能乱

比如左半部分有序时写的是：

```python
nums[left] <= target < nums[mid]
```

这里：

- 左边带等号
- 右边不带等号

是为了避免和前面 `nums[mid] == target` 的判断重复，
同时也防止边界漏掉。

## 算法步骤

1. 定义左右指针 `left = 0`、`right = len(nums) - 1`
2. 当 `left <= right` 时，计算中点 `mid`
3. 如果 `nums[mid] == target`，直接返回 `mid`
4. 判断左半部分是否有序
5. 如果左半部分有序，就判断 `target` 是否落在左半部分范围内
6. 如果右半部分有序，就判断 `target` 是否落在右半部分范围内
7. 根据判断结果移动 `left` 或 `right`
8. 如果循环结束还没找到，返回 `-1`

## 复杂度分析

### 时间复杂度

`O(log n)`

原因是：

- 每一轮都能排除掉一半搜索空间
- 二分查找总共只会进行对数级别的循环次数

### 空间复杂度

`O(1)`

原因是：

- 只使用了 `left`、`right`、`mid` 等常数个变量
- 没有使用额外与输入规模相关的存储空间

## Python 参考实现（详细注释）

```python
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # 如果中点刚好就是目标值，直接返回
            if nums[mid] == target:
                return mid

            # 情况 1：左半部分有序
            if nums[left] <= nums[mid]:
                # 如果 target 落在左半部分的有序区间里，去左边继续找
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # 否则只能去右边找
                    left = mid + 1
            else:
                # 情况 2：右半部分有序
                # 如果 target 落在右半部分的有序区间里，去右边继续找
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    # 否则去左边找
                    right = mid - 1

        return -1
```

## 这段代码最值得记住的地方

最核心的不是普通二分模板本身，
而是这一段判断：

```python
if nums[left] <= nums[mid]:
    if nums[left] <= target < nums[mid]:
        right = mid - 1
    else:
        left = mid + 1
else:
    if nums[mid] < target <= nums[right]:
        left = mid + 1
    else:
        right = mid - 1
```

它体现了这道题最关键的思路：

- 先判断哪一半有序
- 再判断 `target` 是否在那一半里
- 最后舍弃另一半

## 常见错误

### 1. 直接把它当普通二分查找来写

如果只根据：

- `target < nums[mid]`
- `target > nums[mid]`

来决定往左还是往右，
在旋转数组里会出错。

### 2. 没有先判断哪一半有序

这道题最核心的一步就是：

- 先识别有序区间

如果这一步没想清楚，后面的边界更新就很容易乱。

### 3. 区间判断的边界写错

例如：

- 左边写成 `nums[left] < target < nums[mid]`
- 或右边写成 `nums[mid] < target < nums[right]`

都可能把边界值漏掉。

### 4. 忽略“元素互不相同”这个前提

这道题因为没有重复元素，逻辑才比较干净。

如果有重复元素，判断哪一半有序会更复杂，
不能直接照搬这份代码。

### 5. 想先排序再二分

这样会有两个问题：

- 排序后原下标就乱了
- 时间复杂度也不再是 `O(log n)`

## 适合你自己再写一遍的版本

```python
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
```

## 一句话总结

这道题的关键不是死记旋转数组的结论，而是：

**每次二分时先找出哪一半仍然有序，再判断 `target` 是否落在这个有序区间里，从而继续排除一半区间。**
