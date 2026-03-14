# 057. 插入区间

## 所属专题

- 区间

## 题目描述

给你一个 **无重叠的、按照区间起始端点排序** 的区间列表 `intervals`，
其中 `intervals[i] = [start_i, end_i]` 表示第 `i` 个区间的开始和结束。

另外给你一个新区间 `newInterval = [start, end]`。

你需要把 `newInterval` 插入到 `intervals` 中，
并保证插入后的结果仍然满足：

- 按照区间起点升序排列
- 区间之间不重叠
- 如果有重叠，就要把它们合并起来

最后返回插入后的区间列表。

## 示例

### 示例 1

```text
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
```

### 示例 2

```text
输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
```

解释：

- 新区间 `[4,8]` 会和 `[3,5]`、`[6,7]`、`[8,10]` 重叠
- 所以这些区间要合并成 `[3,10]`

### 示例 3

```text
输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]
```

## 题意理解

这道题并不是简单地把一个新区间塞进数组里就结束了。

真正要做的是：

1. 找到 `newInterval` 应该插入的位置
2. 如果它和周围区间有重叠，就把它们合并
3. 最终得到一组仍然有序、且互不重叠的区间

题目已经给了两个很重要的条件：

- 原来的区间已经按起点排好序
- 原来的区间彼此不重叠

这两个条件非常关键，
因为它们意味着：

- 我们不需要重新对所有区间排序
- 也不需要做复杂的数据结构处理
- 只需要从左到右扫描一遍，就能把事情做完

## 最直接的想法：先插进去，再整体合并

最容易想到的办法是：

1. 把 `newInterval` 直接插进 `intervals`
2. 然后把整个数组重新做一遍“合并区间”

这种思路当然能做，
而且逻辑上也没有问题。

比如：

```text
intervals = [[1,3],[6,9]]
newInterval = [2,5]
```

你可以先变成：

```text
[[1,3],[2,5],[6,9]]
```

然后再做一次合并区间，
得到：

```text
[[1,5],[6,9]]
```

但是这里其实有点“绕了一圈”。

因为题目已经保证：

- 原数组有序
- 原数组内部不重叠

所以我们完全可以利用这些条件，
在扫描的过程中直接完成插入和合并，
不必把问题先变复杂再处理。

## 优化思路：一趟扫描，把区间分成三段

这道题最经典的做法是把所有区间分成三类：

### 第 1 类：在新区间左边，且完全不重叠

如果一个区间满足：

```python
intervals[i][1] < newInterval[0]
```

说明：

- 它的结束位置还在新区间起点左边
- 它和新区间完全没有交集

这种区间可以直接加入结果，
因为无论怎么插入，
它都一定出现在新区间前面。

### 第 2 类：和新区间重叠

如果一个区间满足：

```python
intervals[i][0] <= newInterval[1]
```

说明它和当前 `newInterval` 有重叠。

这时候就不能直接放进结果，
而是要把它和 `newInterval` 合并：

- 左边界取两者较小值
- 右边界取两者较大值

也就是：

```python
newInterval[0] = min(newInterval[0], intervals[i][0])
newInterval[1] = max(newInterval[1], intervals[i][1])
```

注意这里的意思是：

- `newInterval` 会在扫描过程中不断“长大”

它最后会变成“新区间和所有重叠区间合并后的结果”。

### 第 3 类：在新区间右边，且完全不重叠

当前面所有重叠区间都处理完之后，
我们就可以先把合并后的 `newInterval` 放进结果。

剩下的区间由于本来就有序，
而且已经不可能再和 `newInterval` 重叠，
所以直接按顺序追加到结果末尾即可。

## 用示例手推一遍

以示例 2 为例：

```text
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
```

### 第 1 段：先处理完全在左边的区间

看 `[1,2]`：

- 它的结束位置 `2 < 4`
- 说明它完全在新区间左边

所以直接加入结果：

```text
result = [[1,2]]
```

再看 `[3,5]`：

- 它的结束位置 `5` 不小于 `4`
- 所以不能归入“左边不重叠区间”

左边这一段到此结束。

### 第 2 段：处理所有和新区间重叠的区间

当前 `newInterval = [4,8]`

#### 和 `[3,5]` 重叠

- 因为 `3 <= 8`
- 所以发生重叠

合并后：

```text
newInterval = [3,8]
```

#### 和 `[6,7]` 重叠

- 因为 `6 <= 8`

合并后：

```text
newInterval = [3,8]
```

#### 和 `[8,10]` 重叠

- 因为 `8 <= 8`

注意这里边界相接也算重叠，
因为新区间要求最后不能有重叠区间存在。

合并后：

```text
newInterval = [3,10]
```

#### 看 `[12,16]`

- 因为 `12 > 10`
- 它已经不和合并后的新区间重叠了

于是重叠区间处理结束。

### 第 3 段：把合并结果和右边区间加入答案

先把当前合并后的新区间加入结果：

```text
result = [[1,2],[3,10]]
```

再把剩余区间按顺序加入：

```text
result = [[1,2],[3,10],[12,16]]
```

这就是最终答案。

## 为什么这样写

### 1. 原数组“有序且不重叠”是核心突破口

如果原区间是乱序的，
或者本来就有重叠，
那这道题会复杂很多。

但现在题目已经给了非常强的前提：

- 有序
- 不重叠

这意味着从左往右看时，
区间和 `newInterval` 的关系只会依次经历：

- 在左边
- 有重叠
- 在右边

不会来回反复。

所以一次线性扫描就够了。

### 2. 不需要单独“找插入位置”

有些同学一看到“插入”，
就会先想着：

- 要不要先二分查找插入位置？

其实这题没必要。

因为即使你找到了插入位置，
后面还是要继续处理重叠合并。

既然最终还是要线性扫描，
那不如直接在扫描过程中：

- 顺手处理左边区间
- 顺手合并重叠区间
- 顺手追加右边区间

一步到位。

### 3. 把 `newInterval` 当成“动态合并结果”非常自然

这题一个很好记的点是：

- 不要把 `newInterval` 看成固定不变的输入
- 而要把它看成“当前合并后的区间”

每遇到一个重叠区间，
就更新它的左右边界。

这样最后把它放进答案时，
它已经是正确的合并结果了。

## 算法步骤

1. 创建结果列表 `result`
2. 用指针 `i` 从左到右扫描 `intervals`
3. 先把所有完全位于 `newInterval` 左侧的区间加入 `result`
4. 接着处理所有与 `newInterval` 重叠的区间
5. 每遇到一个重叠区间，就更新 `newInterval` 的左右边界
6. 重叠区间处理完后，把合并后的 `newInterval` 加入 `result`
7. 最后把剩余所有位于右侧的区间加入 `result`
8. 返回 `result`

## 复杂度分析

### 时间复杂度

`O(n)`

其中 `n` 是区间个数。

原因是：

- 整个数组只会被从左到右扫描一遍
- 每个区间最多只处理一次

### 空间复杂度

如果 **不计算返回结果本身**，
辅助空间复杂度是：

`O(1)`

因为：

- 只使用了少量额外变量，比如 `i`

如果把返回结果 `result` 也算进去，
那么总空间复杂度是：

`O(n)`

因为答案中最多仍然要保存所有区间。

## Python 参考实现（详细注释）

```python
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 用来保存最终答案。
        result = []

        # 指针 i 用来从左到右扫描区间数组。
        i = 0
        n = len(intervals)

        # 第一段：把所有完全在 newInterval 左边、且不重叠的区间直接加入答案。
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 第二段：处理所有和 newInterval 重叠的区间。
        # 这里不断更新 newInterval，让它变成“当前合并后的区间”。
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # 到这里为止，newInterval 已经是合并后的最终区间。
        result.append(newInterval)

        # 第三段：把剩余完全在右边的区间继续加入答案。
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
```

## 这段代码最值得记住的地方

这题最值得记住的，其实就是“三段式扫描”：

```python
while i < n and intervals[i][1] < newInterval[0]:
    ...

while i < n and intervals[i][0] <= newInterval[1]:
    ...

while i < n:
    ...
```

它对应的就是：

1. 左边不重叠
2. 中间重叠并合并
3. 右边不重叠

只要把这三个阶段想清楚，
整道题就很顺。

另外还要记住一点：

- `newInterval` 在中间那一段会不断更新

它不是固定输入，
而是当前合并结果。

## 常见错误

### 1. 把“边界相接”误判为不重叠

例如：

- `[3,5]` 和 `[5,7]`

在这道题里应该合并，
因为它们相接，最终不能留下重叠/相连的碎片区间。

所以重叠判断应该写成：

```python
intervals[i][0] <= newInterval[1]
```

而不是：

```python
intervals[i][0] < newInterval[1]
```

### 2. 先把 `newInterval` 放进结果，再去合并

如果过早把 `newInterval` 先加入答案，
后面处理重叠时就容易把逻辑搞乱，
甚至需要回头修改结果。

更自然的方式是：

- 先扫描并完成合并
- 等 `newInterval` 变成最终区间后，再加入结果

### 3. 忘记把左边不重叠区间先加入结果

这会导致本来应该在新区间前面的区间丢失。

### 4. 合并时只更新一边边界

合并区间时必须同时考虑：

- 左边界取最小值
- 右边界取最大值

如果只更新右边界，
或者只更新左边界，
结果都会错。

### 5. 直接修改输入时没有意识到 `newInterval` 会变化

这里代码里会原地更新：

```python
newInterval[0] = ...
newInterval[1] = ...
```

这在题目里通常没问题，
但你要明确知道：

- 这不是在保留原始 `newInterval`
- 而是在构造合并后的新区间

## 适合你自己再写一遍的版本

如果你准备先记一个最稳定的版本，
可以直接记这版：

```python
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result
```

## 一句话总结

这道题的关键是：

**利用原区间“有序且互不重叠”的性质，把所有区间分成左边不重叠、 中间重叠、右边不重叠三段，一趟扫描完成插入和合并。**
