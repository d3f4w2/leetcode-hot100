# 042. 接雨水

## 所属专题

- 双指针

## 题目描述

给定 `n` 个非负整数 `height`，每个数字表示宽度为 `1` 的柱子的高度。

下雨之后，柱子之间可能会积水。请你计算整个高度图最多能接多少雨水。

## 示例

### 示例 1

```text
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：这个高度图一共可以接 6 个单位的雨水。
```

### 示例 2

```text
输入：height = [4,2,0,3,2,5]
输出：9
```

## 题意理解

这道题表面上是在问“总共能接多少雨水”，
但真正要想清楚的是：

- 每一列上方最多能存多少水
- 然后把所有列的水量加起来

对于下标 `i` 这一列来说，它上方能不能存水，取决于两边有没有足够高的“挡板”。

如果：

- 左边最高柱子是 `left_max`
- 右边最高柱子是 `right_max`

那么第 `i` 列最多能接的水就是：

```text
min(left_max, right_max) - height[i]
```

但前提是这个值要大于 `0`。

也就是说，这题的本质是：

**对每个位置，找到它左边最高的柱子和右边最高的柱子，较矮的那一边决定这格水位。**

## 最直接的想法：逐列向左右找最高柱子

最朴素的做法很容易想到：

- 枚举每一个位置 `i`
- 向左扫描，找到 `i` 左边的最高柱子
- 向右扫描，找到 `i` 右边的最高柱子
- 用 `min(left_max, right_max) - height[i]` 算出这一列的积水

这样一定能做出来。

但是问题也很明显：

- 一共有 `n` 个位置
- 每个位置都可能要向左扫一遍、向右扫一遍

所以时间复杂度会变成：

```text
O(n^2)
```

这道题是经典题，当然有更好的线性解法。

## 优化思路：双指针

这题最值得掌握的主解法就是双指针。

### 第一步：两边同时向中间靠拢

我们设置两个指针：

- `left = 0`
- `right = len(height) - 1`

同时再维护两个变量：

- `left_max`：从左边走到当前位置时，见过的最高柱子
- `right_max`：从右边走到当前位置时，见过的最高柱子

### 第二步：什么时候可以“结算”当前位置

关键问题不是“哪边高”，
而是：

**当前哪一边的最大挡板更小，就先结算哪一边。**

为什么？

假设当前有：

```text
left_max < right_max
```

这说明左边这一列的最终水位已经可以确定了。

因为：

- 它左边的最高挡板就是 `left_max`
- 它右边至少还有一个高度不低于 `right_max` 的挡板
- 而 `right_max` 又比 `left_max` 更高

所以左边当前位置能装多少水，只会由较矮的 `left_max` 决定：

```text
left_max - height[left]
```

这时就可以放心结算 `left` 位置，然后让 `left += 1`。

反过来，如果：

```text
left_max >= right_max
```

那就说明右边当前位置的水位已经可以确定，
此时应该结算右边，然后让 `right -= 1`。

### 第三步：为什么这样不会漏

双指针并不是“碰运气”地缩范围，
而是在每一步都做了一次安全结算：

- 较小的一侧，水位已经确定
- 较大的一侧，暂时还不能完全确定

所以每一轮都能正确处理掉一个位置，
而且不会重复处理，也不会漏掉答案。

## 用示例手推一遍

以示例 1 为例：

```text
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

初始化：

- `left = 0`
- `right = 11`
- `left_max = 0`
- `right_max = 0`
- `water = 0`

下面看几个关键步骤。

### 第 1 步

- `left = 0`，`height[left] = 0`
- `right = 11`，`height[right] = 1`
- 更新后：`left_max = 0`，`right_max = 1`

因为：

```text
left_max < right_max
```

所以可以结算左边：

```text
water += left_max - height[left] = 0 - 0 = 0
```

然后：

```text
left += 1
```

### 第 2 步

- `left = 1`，`height[left] = 1`
- `right = 11`，`height[right] = 1`
- 更新后：`left_max = 1`，`right_max = 1`

此时右边先结算：

```text
water += right_max - height[right] = 1 - 1 = 0
right -= 1
```

### 第 3 步

- `left = 1`
- `right = 10`
- 更新后：`left_max = 1`，`right_max = 2`

因为左边挡板更低，所以结算左边：

```text
water += 1 - 1 = 0
left += 1
```

### 第 4 步

- `left = 2`，`height[left] = 0`
- `left_max = 1`，`right_max = 2`

继续结算左边：

```text
water += 1 - 0 = 1
```

这说明下标 `2` 这一列能接 `1` 格水。

### 后面的关键结算

继续按同样方式推进，会得到：

- 下标 `4` 接 `1`
- 下标 `5` 接 `2`
- 下标 `6` 接 `1`
- 下标 `9` 接 `1`

再加上下标 `2` 的 `1`，
总水量就是：

```text
1 + 1 + 2 + 1 + 1 = 6
```

这正好是答案。

## 为什么这样写是对的

双指针这题最核心的不是记代码，
而是记住下面这个不变式：

- `left_max` 始终是区间 `[0, left]` 内的最高柱子
- `right_max` 始终是区间 `[right, n - 1]` 内的最高柱子

然后分两种情况：

### 情况 1：`left_max < right_max`

这时 `left` 位置右边一定存在一个不低于 `right_max` 的挡板，
所以右边的限制一定不比左边更紧。

因此：

```text
min(left_max, right_max) = left_max
```

当前位置 `left` 的积水就已经完全确定为：

```text
left_max - height[left]
```

可以立刻加入答案，并移动 `left`。

### 情况 2：`left_max >= right_max`

同理，右边当前位置的积水已经完全由 `right_max` 决定：

```text
right_max - height[right]
```

可以立刻加入答案，并移动 `right`。

所以每一轮都能安全地处理一侧，
整个过程结束后，所有位置都恰好被计算一次。

## 另一种可行思路：单调栈

这题还有一种很经典的解法是单调栈。

思路是：

- 栈里存柱子的下标
- 保持栈中柱子高度单调递减
- 一旦遇到一个更高的柱子，就说明找到了某个“凹槽”的右边界
- 弹出栈顶作为凹槽底部，再用新的栈顶作为左边界，计算这一层能接多少水

单调栈同样能做到：

- 时间复杂度 `O(n)`
- 空间复杂度 `O(n)`

不过从当前这个专题来看，
这题最推荐先把双指针版本吃透。

## 算法步骤

1. 如果数组为空，直接返回 `0`
2. 初始化两个指针：`left = 0`，`right = len(height) - 1`
3. 初始化两个最大值：`left_max = 0`，`right_max = 0`
4. 初始化答案：`water = 0`
5. 当 `left < right` 时循环：
6. 先更新 `left_max` 和 `right_max`
7. 如果 `left_max < right_max`，说明左边当前位置可结算，把 `left_max - height[left]` 加入答案，并让 `left += 1`
8. 否则说明右边当前位置可结算，把 `right_max - height[right]` 加入答案，并让 `right -= 1`
9. 循环结束后返回 `water`

## 复杂度分析

### 时间复杂度

`O(n)`

原因是：

- 两个指针都只会从两端向中间移动
- 每个位置最多只会被处理一次

### 空间复杂度

`O(1)`

原因是：

- 只使用了几个额外变量
- 没有使用与输入规模相关的额外数组或栈

补充：

- 如果使用单调栈解法，空间复杂度会是 `O(n)`

## Python 参考实现（详细注释）

```python
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1

        # left_max 表示从左边走到当前 left 时见过的最高柱子
        # right_max 表示从右边走到当前 right 时见过的最高柱子
        left_max = 0
        right_max = 0

        # water 用来累计总积水量
        water = 0

        while left < right:
            # 先把当前两端的最高挡板信息更新出来
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            # 哪一侧的最高挡板更低，就先结算哪一侧。
            # 因为较低的一侧已经决定了那一格的最高水位。
            if left_max < right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1

        return water
```

## 常见错误

### 1. 对每个位置都重新向左右扫描

这样虽然能做出来，
但时间复杂度是 `O(n^2)`，
这道题更值得掌握的是线性做法。

### 2. 没有先更新 `left_max` 和 `right_max`

如果你先直接写：

```python
water += left_max - height[left]
```

再去更新 `left_max`，
就可能把当前位置本身的高度信息漏掉，导致计算错误。

更稳妥的顺序是：

1. 先更新当前两侧最大值
2. 再决定结算哪一边

### 3. 不明白为什么能只结算一边

这题最容易卡住的地方就在这里。

一定要记住：

- 不是左右两边都同时确定
- 而是哪一边的“较小挡板”先确定，就先结算哪一边

### 4. 以为积水只会出现在“最低点”

其实不是。

每个位置都可能有自己的积水量，
最后答案是把所有位置上方的水量逐列相加。

## 适合自己默写的精简版本

```python
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1

        return water
```

## 一句话总结

这道题的关键是：

**用双指针从两端向中间收缩，同时维护左右最高挡板；哪一边的最高挡板更低，就先结算哪一边，因为那一侧当前位置的水位已经可以确定。**
