# 034. 在排序数组中查找元素的第一个和最后一个位置

## 所属专题

- 二分查找

## 题目描述

给你一个按照 **非递减顺序** 排列的整数数组 `nums`，和一个目标值 `target`。

请你找出给定目标值在数组中的：

- 开始位置
- 结束位置

如果数组中不存在目标值 `target`，返回：

```text
[-1, -1]
```

并且你必须设计并实现时间复杂度为 `O(log n)` 的算法。

## 示例

### 示例 1

```text
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
```

### 示例 2

```text
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
```

### 示例 3

```text
输入：nums = [], target = 0
输出：[-1,-1]
```

## 题意理解

这道题不是单纯让我们判断：

- `target` 在不在数组里

而是要进一步找到：

- 它第一次出现的位置
- 它最后一次出现的位置

例如：

```text
nums = [5,7,7,8,8,10], target = 8
```

数字 `8` 出现了两次，位置分别是：

- 下标 `3`
- 下标 `4`

所以答案是：

```text
[3,4]
```

如果数组里没有这个数，比如 `target = 6`，
那就返回：

```text
[-1,-1]
```

另外，题目明确要求：

- 时间复杂度必须是 `O(log n)`

这就意味着：

- 不能从左到右线性扫描
- 基本上就是在暗示我们必须使用二分查找

## 最直接的想法：线性扫描

最容易想到的方法是：

1. 从左到右找第一个等于 `target` 的位置
2. 再继续往后找最后一个等于 `target` 的位置

或者：

- 先找到所有等于 `target` 的元素
- 再取最左和最右的位置

这个方法逻辑不难，确实能做出来。

但是问题是：

- 最坏情况下要把整个数组扫一遍

所以时间复杂度是：

`O(n)`

不满足题目要求的 `O(log n)`。

## 优化思路：做两次二分查找

这是这道题最经典的做法。

### 核心想法

我们不直接找：

- “第一个等于 `target` 的位置”
- “最后一个等于 `target` 的位置”

而是转换成两个更适合二分的问题：

1. 找到第一个 **大于等于 `target`** 的位置
2. 找到第一个 **大于 `target`** 的位置

为什么这样转化？

因为二分查找特别适合处理这种“边界位置”问题。

### 第一个边界：第一个大于等于 `target` 的位置

这个位置其实就是：

- `target` 如果存在时的最左位置

例如：

```text
nums = [5,7,7,8,8,10], target = 8
```

第一个大于等于 `8` 的位置是：

- 下标 `3`

这恰好就是 `8` 第一次出现的位置。

### 第二个边界：第一个大于 `target` 的位置

这个位置表示：

- 所有等于 `target` 的元素，到这里就结束了

所以：

```text
最后一个等于 target 的位置 = 第一个大于 target 的位置 - 1
```

还是上面的例子：

- 第一个大于 `8` 的位置是下标 `5`（值为 `10`）
- 所以最后一个等于 `8` 的位置就是：`5 - 1 = 4`

答案就是：

```text
[3,4]
```

## 为什么这样做是对的

### 1. 排序数组天然适合找边界

因为数组是非递减排列，所以一旦某个位置满足某个条件，
它左边和右边往往会呈现出明确的规律。

例如对于条件：

```text
nums[i] >= target
```

数组会被分成两段：

- 左边一段都不满足
- 右边一段都满足

这种“前一段假、后一段真”的结构，正是二分最擅长处理的。

### 2. 不直接找相等，而是找边界，更稳定

如果数组里有很多重复元素，
直接二分到一个等于 `target` 的位置，并不能立刻知道：

- 它是不是最左的
- 它是不是最右的

所以更稳妥的做法是：

- 直接找“最左满足条件的位置”

这就是边界二分。

### 3. 两次边界二分就能完整确定区间

第一次边界给你：

- 起点

第二次边界给你：

- 终点的后一位

于是区间就完整确定了。

## 用示例手推一遍

以示例 1 为例：

```text
nums = [5,7,7,8,8,10], target = 8
```

### 第 1 次二分：找第一个大于等于 `8` 的位置

目标是找到最左边那个满足：

```text
nums[i] >= 8
```

最终会停在：

```text
left = 3
```

因为：

- `nums[3] = 8`
- 并且它是第一个满足条件的位置

所以这个位置就是：

- `8` 的开始位置

### 第 2 次二分：找第一个大于 `8` 的位置

这次目标是最左边满足：

```text
nums[i] > 8
```

最终会停在：

```text
left = 5
```

因为：

- `nums[5] = 10`
- 它是第一个严格大于 `8` 的位置

所以最后一个 `8` 的位置就是：

```text
5 - 1 = 4
```

最终答案：

```text
[3,4]
```

## target 不存在时会怎样

例如：

```text
nums = [5,7,7,8,8,10], target = 6
```

第一次二分会找到：

- 第一个大于等于 `6` 的位置，也就是下标 `1`

但是：

```text
nums[1] = 7
```

它并不等于 `6`。

这就说明：

- 数组中根本没有 `6`

所以直接返回：

```text
[-1,-1]
```

这一步判断非常重要。

## 算法步骤

1. 用二分查找找到第一个大于等于 `target` 的位置 `first`
2. 如果 `first` 越界，或者 `nums[first] != target`，说明目标不存在，直接返回 `[-1, -1]`
3. 再用二分查找找到第一个大于 `target` 的位置
4. 令这个位置减一，得到最后一次出现的位置 `last`
5. 返回 `[first, last]`

## 复杂度分析

### 时间复杂度

`O(log n)`

原因：

- 做了两次二分查找
- 每次二分都是 `O(log n)`

总复杂度仍然是 `O(log n)`。

### 空间复杂度

`O(1)`

原因：

- 只使用了常数个额外变量
- 没有额外开与输入规模相关的空间

## Python 参考实现（详细注释）

```python
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 找到第一个大于等于 target 的位置。
        def find_first(nums: List[int], target: int) -> int:
            left, right = 0, len(nums)

            # 使用左闭右开区间 [left, right)。
            while left < right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    # mid 一定不可能是答案，去右半边继续找。
                    left = mid + 1
                else:
                    # nums[mid] >= target，mid 可能是答案，收缩右边界。
                    right = mid

            # 循环结束后，left 就是第一个 >= target 的位置。
            if left < len(nums) and nums[left] == target:
                return left
            return -1

        # 找到第一个大于 target 的位置，再减一得到最后一次出现的位置。
        def find_last(nums: List[int], target: int) -> int:
            left, right = 0, len(nums)

            while left < right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    # nums[mid] 还不够大，所以答案一定在右边。
                    left = mid + 1
                else:
                    # nums[mid] > target，mid 可能是“第一个大于 target”的位置。
                    right = mid

            # 此时 left 指向第一个 > target 的位置。
            # 所以最后一个 == target 的位置是 left - 1。
            if left > 0 and nums[left - 1] == target:
                return left - 1
            return -1

        first = find_first(nums, target)

        # 如果最左位置都找不到，说明目标根本不存在。
        if first == -1:
            return [-1, -1]

        last = find_last(nums, target)
        return [first, last]
```

## 这段代码最值得记住的地方

你在自己手写的时候，重点记住下面这条主线：

```python
def find_first(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left if left < len(nums) and nums[left] == target else -1

def find_last(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left - 1 if left > 0 and nums[left - 1] == target else -1
```

本质上就是一句话：

**先找最左边的 `target`，再找最右边的 `target`，而这两个位置都可以转化成“边界二分”问题。**

## 常见错误

### 1. 找到了一个 `target` 就直接向两边扩散

这样虽然能做出来，
但最坏情况下会退化成：

`O(n)`

不符合题目要求。

### 2. 二分区间写乱

这题推荐固定写法：

- 左闭右开区间 `[left, right)`

这样边界更清楚，尤其适合写“第一个满足条件的位置”。

### 3. 忘记判断 `target` 是否真的存在

第一次二分找到的是：

- 第一个大于等于 `target` 的位置

但这并不自动保证这个位置上的值就是 `target`。

所以必须检查：

```python
left < len(nums) and nums[left] == target
```

### 4. 最后一个位置的计算写错

第二次二分找到的是：

- 第一个大于 `target` 的位置

所以真正的最后位置是：

```python
left - 1
```

不是 `left` 本身。

### 5. 数组为空时越界

比如：

```text
nums = []
```

这时所有访问下标的地方都要格外小心。

## 适合你自己再写一遍的版本

如果你准备在自己的 `.ipy` 文件里默写，建议先记住下面这个精简版本：

```python
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums: List[int], target: int) -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left if left < len(nums) and nums[left] == target else -1

        def find_last(nums: List[int], target: int) -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left - 1 if left > 0 and nums[left - 1] == target else -1

        first = find_first(nums, target)
        if first == -1:
            return [-1, -1]

        last = find_last(nums, target)
        return [first, last]
```

## 一句话总结

这道题的关键不是普通二分“找一个值”，而是：

**把开始位置和结束位置都转换成“边界查找”，分别用两次二分去找第一个满足条件的位置。**
