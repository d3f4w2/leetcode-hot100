# 139. 单词拆分

## 所属专题
- 动态规划

## 题目描述

给你一个字符串 `s` 和一个字符串列表 `wordDict` 作为字典。

请你判断：

- 是否可以利用字典中的单词
- 把字符串 `s` 完整地拼接出来

注意：

- 不要求字典中的单词全部都使用
- 字典中的单词可以重复使用

## 示例

### 示例 1

```text
输入：s = leetcode, wordDict = [leet, code]
输出：true
解释：leetcode = leet + code
```

### 示例 2

```text
输入：s = applepenapple, wordDict = [apple, pen]
输出：true
解释：applepenapple = apple + pen + apple
     注意字典中的单词可以重复使用。
```

### 示例 3

```text
输入：s = catsandog, wordDict = [cats, dog, sand, and, cat]
输出：false
解释：无法把整个字符串完整拆分成字典中的单词。
```

## 题意理解

这道题不是问：

- 字典里有没有某个单词

而是问：

- 字符串 `s` 能不能被切成若干段
- 并且每一段都恰好出现在 `wordDict` 中

也就是说，我们要做的是：

- 尝试在字符串中间不断“切一刀”
- 看前半部分能不能合法拆分
- 看后半部分是不是字典里的一个单词

只要存在一种切法成立，答案就是 `true`。

## 为什么适合用动态规划

比如字符串是：

```text
leetcode
```

当你判断整个字符串能不能拆分时，
会不断遇到类似的问题：

- 前 4 个字符能不能拆分
- 前 5 个字符能不能拆分
- 前 6 个字符能不能拆分

这些“前缀是否可拆分”的问题会被反复使用。

这正是动态规划的典型特征：

- 大问题依赖小问题
- 小问题会重复出现

所以我们可以把每个前缀的结果先存下来，
后面直接复用。

## 动态规划定义

定义：

```text
dp[i] = 字符串 s 的前 i 个字符是否可以被成功拆分
```

这里要特别注意：

- `dp[i]` 表示的是“前 `i` 个字符”
- 不是下标为 `i` 的字符

例如：

- `dp[0]` 表示空字符串
- `dp[4]` 表示 `s[0:4]`
- `dp[n]` 表示整个字符串 `s`

## 为什么 `dp[0] = True`

```text
dp[0] = True
```

它表示：

- 空字符串是可以被成功拆分的

这不是在说空字符串是一个单词，
而是在说：

- 当我们切到某个位置时
- 如果前面正好已经全部合法拆分完了
- 那么这个状态应该被视为“成立”

它是整道题的起点。

## 状态转移方程

如果我们想求 `dp[i]`，
就要尝试最后一段单词从哪里开始。

假设最后一段是：

```text
s[j:i]
```

那么要让 `dp[i]` 成立，必须同时满足两件事：

1. 前面的部分 `s[0:j]` 可以被成功拆分，也就是 `dp[j] == True`
2. 最后一段 `s[j:i]` 本身就在字典中

所以状态转移就是：

```text
dp[i] = dp[j] and s[j:i] in wordDict
```

其中：

```text
0 <= j < i
```

只要存在某个 `j` 满足条件，
就可以说明：

```text
dp[i] = True
```

## 为什么切片写成 `s[j:i]`

Python 的切片规则是：

```python
s[a:b]
```

表示：

- 取下标从 `a` 开始
- 到下标 `b - 1` 结束
- 左闭右开

所以：

- `s[0:4]` 表示前 4 个字符
- `s[j:i]` 表示从第 `j` 个字符到第 `i - 1` 个字符

这恰好对应“最后一个单词”的范围。

## 转移过程怎么理解

对于每个位置 `i`，
我们都去枚举一个分割点 `j`：

- 左边：`s[0:j]`
- 右边：`s[j:i]`

然后问：

- 左边以前能不能拆出来？
- 右边这段是不是一个合法单词？

如果都满足，
说明前 `i` 个字符可以被拆分。

也就是：

```python
if dp[j] and s[j:i] in word_set:
    dp[i] = True
```

## 用示例手推一遍

以：

```text
s = leetcode
wordDict = [leet, code]
```

为例。

字符串长度是 `8`，
所以我们需要：

```text
dp[0] 到 dp[8]
```

初始状态：

```text
dp = [True, False, False, False, False, False, False, False, False]
```

### 计算 `dp[1]`

前 1 个字符是：

```text
l
```

无论怎么切，`l` 都不在字典里，
所以：

```text
dp[1] = False
```

### 计算 `dp[2]`

前 2 个字符是：

```text
le
```

也不能拆成字典里的单词，
所以：

```text
dp[2] = False
```

### 计算 `dp[3]`

前 3 个字符是：

```text
lee
```

仍然不行：

```text
dp[3] = False
```

### 计算 `dp[4]`

前 4 个字符是：

```text
leet
```

当 `j = 0` 时：

- `dp[0] = True`
- `s[0:4] = leet` 在字典中

所以：

```text
dp[4] = True
```

### 计算 `dp[5]`、`dp[6]`、`dp[7]`

这几个前缀都无法拆成合法单词组合，
所以仍然是：

```text
dp[5] = dp[6] = dp[7] = False
```

### 计算 `dp[8]`

前 8 个字符是整个字符串：

```text
leetcode
```

当 `j = 4` 时：

- `dp[4] = True`
- `s[4:8] = code` 在字典中

所以：

```text
dp[8] = True
```

最终答案是：

```text
True
```

## 为什么这道题要用两层循环

外层循环：

```python
for i in range(1, n + 1):
```

表示：

- 依次求出每个前缀 `s[0:i]` 能不能被拆分

内层循环：

```python
for j in range(i):
```

表示：

- 枚举最后一刀切在哪里

所以这两层循环的配合本质上就是：

- 固定终点 `i`
- 尝试所有可能的起点 `j`
- 看 `s[j:i]` 能不能作为最后一个单词

## 为什么要把 `wordDict` 变成集合

```python
word_set = set(wordDict)
```

因为我们会频繁判断：

```python
s[j:i] in word_set
```

如果 `wordDict` 还是列表，
每次查找都要从头到尾找，效率较低。

而集合的查找通常更快，
所以这是很常见的优化。

## 算法步骤

1. 先把 `wordDict` 转成集合 `word_set`
2. 定义 `dp[i]` 表示前 `i` 个字符能否被拆分
3. 初始化 `dp[0] = True`
4. 从 `i = 1` 遍历到 `n`
5. 对每个 `i`，枚举分割点 `j`
6. 如果 `dp[j]` 为真，并且 `s[j:i]` 在字典中，就令 `dp[i] = True`
7. 最终返回 `dp[n]`

## 复杂度分析

### 时间复杂度

通常写作：`O(n^2)`

因为：

- 外层枚举 `i`
- 内层枚举 `j`

如果严格按 Python 切片成本来算，
`s[j:i]` 会产生新字符串，
实际开销会更高。

但在面试和大多数题解中，
这道题通常记为：

```text
O(n^2)
```

### 空间复杂度

`O(n)`

因为：

- 使用了一个长度为 `n + 1` 的 `dp` 数组

## Python 参考实现（详细注释）

```python
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        # dp[i] 表示前 i 个字符能否被成功拆分
        dp = [False] * (n + 1)

        # 空字符串可以被认为是“已经成功拆分”
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                # 如果前面的部分可以拆分，且最后一段在字典中
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
```

## 这段代码最值得记住的地方

核心判断只有一句：

```python
if dp[j] and s[j:i] in word_set:
    dp[i] = True
```

它表达的就是：

- 前面已经能拆出来
- 最后一段也是合法单词
- 那么当前前缀就能拆出来

## 常见错误

### 1. 把 `dp[i]` 理解错

很多人会误以为：

```text
dp[i] = 第 i 个字符能不能拆分
```

这是错的。

正确含义是：

```text
dp[i] = 前 i 个字符能不能拆分
```

### 2. 忘记设置 `dp[0] = True`

如果没有这个起点，
很多本来能成立的状态就永远推不出来。

例如：

```python
s[0:4] = leet
```

即使 `leet` 在字典中，
你也需要 `dp[0]` 为真，
才能推出 `dp[4] = True`。

### 3. 把切片边界写错

Python 切片是左闭右开：

```python
s[j:i]
```

表示取到 `i - 1` 为止。

不要把它误写成别的区间含义。

### 4. 不把字典转成集合

如果直接写：

```python
s[j:i] in wordDict
```

逻辑上没问题，
但查找效率通常更差。

### 5. 找到合法拆分后没有及时 `break`

一旦 `dp[i]` 已经确定为 `True`，
后面就没必要继续枚举 `j` 了。

及时 `break` 可以减少不必要的判断。

## 适合自己默写的精简版

```python
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
```

## 一句话总结

这道题的关键是：

**用 `dp[i]` 记录前 `i` 个字符能否被拆分，再枚举最后一刀的位置 `j`，检查前半部分是否可拆、后半部分是否是合法单词。**
