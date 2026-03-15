# 151. 反转字符串中的单词

## 所属专题

- 双指针

## 题目描述

给你一个字符串 `s`，请你反转字符串中 **单词** 的顺序。

单词是由非空格字符组成的字符串。`s` 中使用至少一个空格将字符串中的单词分隔开。

返回 **单词顺序颠倒且单词之间用单个空格连接** 的结果字符串。

注意：

- 输入字符串 `s` 中可能存在前导空格
- 输入字符串 `s` 中可能存在尾随空格
- 单词之间可能存在多个空格
- 返回结果中，单词之间只能保留一个空格
- 返回结果中，不能有前导空格和尾随空格

## 示例

### 示例 1

```text
输入：s = "the sky is blue"
输出："blue is sky the"
```

### 示例 2

```text
输入：s = "  hello world  "
输出："world hello"
解释：反转后的字符串中不能有前导空格和尾随空格。
```

### 示例 3

```text
输入：s = "a good   example"
输出："example good a"
解释：单词之间如果有多个空格，结果中只能保留一个空格。
```

## 题意理解

这道题反转的不是：

- 每个字符的位置

而是：

- **单词之间的顺序**

比如：

```text
s = "the sky is blue"
```

题目不是要得到：

```text
"eulb si yks eht"
```

而是要得到：

```text
"blue is sky the"
```

所以有两个关键点必须同时满足：

1. 单词顺序要反过来
2. 空格格式要被规范化

也就是说，最终答案中：

- 前后不能有空格
- 单词之间只能有一个空格

这也是这道题真正麻烦的地方：

- 不是单纯做一个反转
- 还要顺手把多余空格处理干净

## 最直接的想法：`split()` + 反转 + `join()`

Python 里最容易想到的写法其实非常直接：

1. 先用 `s.split()` 把单词拆出来
2. 再把单词顺序反过来
3. 最后用一个空格拼接起来

例如：

```python
return " ".join(reversed(s.split()))
```

这个写法为什么好用？

- `split()` 不传参数时，会自动忽略前导空格、尾随空格和多个连续空格
- `reversed()` 可以把单词顺序倒过来
- `" ".join(...)` 可以统一用单个空格拼接结果

这个方法很适合面试里先快速写出正确答案。

但是如果继续往下想，会发现它本质上是：

- 先把所有单词重新拆出来
- 再重新构造一个新字符串

空间上并不“原地”。

所以如果我们想训练更扎实的字符串处理能力，就可以继续看下面这个更经典的思路。

## 优化思路：双指针清空格 + 整体反转 + 单词反转

这道题的经典做法可以分成三步：

1. 先去掉多余空格，只保留单词之间的一个空格
2. 再把整个字符串整体反转
3. 最后把每个单词单独反转回来

### 第一步：先清理多余空格

假设原字符串是：

```text
"  the sky   is blue  "
```

清理完多余空格后，先变成：

```text
"the sky is blue"
```

这样做的原因很简单：

- 如果不先把空格规范化，后面反转时就会把一堆无意义的空格也带进去
- 最终输出要求本来就只能保留一个空格

这里可以用双指针：

- `fast` 负责扫描原字符串
- `slow` 负责把有效字符写回前面

本质上就是一边读，一边把“合法内容”压缩到前面去。

### 第二步：反转整个字符串

把：

```text
"the sky is blue"
```

整体反转后变成：

```text
"eulb si yks eht"
```

你会发现：

- 单词顺序确实已经反过来了
- 但是每个单词内部的字符顺序也乱了

也就是说，此时：

- `blue` 变成了 `eulb`
- `sky` 变成了 `yks`

### 第三步：把每个单词再反转回来

然后我们再逐个扫描单词区间，把每个单词内部单独反转一次：

```text
"eulb si yks eht"
```

变成：

```text
"blue is sky the"
```

这样就同时实现了：

- 单词顺序反转
- 单词内部字符恢复正常

这就是这道题最经典的核心思想。

## 用示例手推一遍

我们用这个更能体现空格处理过程的例子：

```text
s = "  the sky   is blue  "
```

### 第 1 步：清理多余空格

用双指针压缩后，字符串有效部分变成：

```text
"the sky is blue"
```

现在：

- 没有前导空格
- 没有尾随空格
- 单词之间都只有一个空格

### 第 2 步：反转整个字符串

整体反转后得到：

```text
"eulb si yks eht"
```

这时候单词顺序已经倒过来了，
但每个单词内部还没恢复。

### 第 3 步：逐个单词反转

先反转 `eulb`：

```text
"blue si yks eht"
```

再反转 `si`：

```text
"blue is yks eht"
```

再反转 `yks`：

```text
"blue is sky eht"
```

最后反转 `eht`：

```text
"blue is sky the"
```

最终答案就是：

```text
"blue is sky the"
```

## 为什么这样写

### 1. 先整体反转，才能一次性把单词顺序倒过来

如果我们直接看单词顺序：

- 原来是 `the sky is blue`
- 目标是 `blue is sky the`

整体反转之后，原本最右边的单词自然会跑到最左边，
所以这是最快把“单词顺序”翻转过来的方法。

### 2. 整体反转之后，单词内部会被打乱

例如：

- `blue` 变成 `eulb`

所以还必须对每个单词区间再反转一次，
把字符顺序恢复过来。

### 3. 双指针很适合处理空格压缩

对于多余空格，我们不需要真的删来删去，
而是可以：

- 用一个指针读原内容
- 用一个指针写有效内容

这样逻辑清楚，也很符合这道题“原地处理字符序列”的思路。

### 4. 反转区间本身就是双指针经典场景

无论是：

- 反转整个字符串
- 还是反转某个单词

本质上都可以用：

- 左指针
- 右指针

从两端向中间收缩完成交换。

所以这题虽然是字符串题，
但它的核心技巧其实就是双指针。

## 算法步骤

1. 先把字符串转换成字符列表，方便做区间交换
2. 用快慢指针去掉前导空格、尾随空格和中间多余空格
3. 只保留压缩后的有效字符部分
4. 反转整个字符列表
5. 从左到右扫描每个单词的边界
6. 每遇到一个完整单词，就把这个单词区间再次反转
7. 最后把字符列表拼接成字符串并返回

## 复杂度分析

### 时间复杂度

`O(n)`

原因是：

- 清理空格扫描一遍
- 整体反转扫描一遍
- 逐词反转再扫描一遍

虽然看起来有多个步骤，
但每个字符处理次数都是常数级，
所以总时间复杂度仍然是 `O(n)`。

### 空间复杂度

Python 实现通常记为：

`O(n)`

原因是：

- Python 的字符串是不可变对象
- 我们通常需要先转成字符列表再处理
- 最后 `join` 时也会重新构造结果字符串

如果是在支持“可变字符数组原地修改”的语言环境里，
这套核心思路可以做到额外空间 `O(1)`。

## Python 参考实现（详细注释）

```python
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        # Python 字符串不可变，先转成字符列表，
        # 这样后面才能做区间反转和原地压缩。
        chars = list(s)

        # 用双指针去掉多余空格，返回压缩后的有效长度。
        valid_length = self.remove_extra_spaces(chars)

        # 只保留真正有效的那一段字符。
        chars = chars[:valid_length]

        # 如果原字符串全是空格，压缩后会变成空串。
        if not chars:
            return ""

        # 第一步：先反转整个字符串，
        # 让单词顺序整体颠倒。
        self.reverse(chars, 0, len(chars) - 1)

        # 第二步：再把每个单词单独反转回来。
        start = 0

        # end 走到空格或结尾时，说明找到了一个完整单词。
        for end in range(len(chars) + 1):
            if end == len(chars) or chars[end] == " ":
                self.reverse(chars, start, end - 1)
                start = end + 1

        return "".join(chars)

    def remove_extra_spaces(self, chars: List[str]) -> int:
        # fast 负责读原字符，slow 负责写回有效字符。
        fast = 0
        slow = 0
        n = len(chars)

        # 先跳过开头所有空格。
        while fast < n and chars[fast] == " ":
            fast += 1

        while fast < n:
            if chars[fast] != " ":
                # 普通字符直接保留。
                chars[slow] = chars[fast]
                slow += 1
            else:
                # 当前读到空格时，只在前一个保留字符不是空格的情况下，
                # 才保留这个空格，从而把连续空格压成一个。
                if slow > 0 and chars[slow - 1] != " ":
                    chars[slow] = chars[fast]
                    slow += 1

            fast += 1

        # 如果最后一个保留字符是空格，要再去掉它，
        # 这样就不会留下尾随空格。
        if slow > 0 and chars[slow - 1] == " ":
            slow -= 1

        return slow

    def reverse(self, chars: List[str], left: int, right: int) -> None:
        # 用双指针原地反转区间 [left, right]。
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
```

## 这段代码最值得记住的地方

如果你只想先记住这道题的主线，可以抓住这三件事：

1. 先压缩空格
2. 再整体反转
3. 最后逐词反转

也就是：

```python
chars = list(s)
valid_length = self.remove_extra_spaces(chars)
chars = chars[:valid_length]

self.reverse(chars, 0, len(chars) - 1)

start = 0
for end in range(len(chars) + 1):
    if end == len(chars) or chars[end] == " ":
        self.reverse(chars, start, end - 1)
        start = end + 1
```

你可以把它理解成一句话：

**先把格式整理干净，再把整串翻过来，最后把每个单词扶正。**

## 常见错误

### 1. 直接写 `s[::-1]`

这只会把字符整体倒过来，
得到的是：

```text
"eulb si yks eht"
```

而不是题目要的：

```text
"blue is sky the"
```

### 2. 用 `split(" ")` 而不是 `split()`

很多人会写：

```python
s.split(" ")
```

这样遇到多个连续空格时，会拆出很多空字符串。

而题目这道题里更稳妥的写法是：

```python
s.split()
```

它会自动帮你处理多余空格。

### 3. 忘了处理前导空格、尾随空格和多个空格

题目的陷阱就在这里。

不是只把单词顺序反过来就结束了，
还要保证最终结果：

- 前后没有空格
- 中间只有一个空格

### 4. 整体反转后，忘了把每个单词再反转回来

整体反转只能解决：

- 单词顺序

不能解决：

- 单词内部字符顺序

所以“逐词反转”这一步绝对不能漏。

### 5. 扫描单词边界时下标写错

在这类题里最容易错的地方是：

- 到底什么时候算一个单词结束
- 反转区间到底是 `[start, end]` 还是 `[start, end - 1]`

如果 `end` 指向的是空格，
那真正单词的结尾就应该是：

```python
end - 1
```

## 适合自己默写的精简版本

```python
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = self.remove_extra_spaces(chars)
        chars = chars[:n]

        if not chars:
            return ""

        self.reverse(chars, 0, len(chars) - 1)

        start = 0
        for end in range(len(chars) + 1):
            if end == len(chars) or chars[end] == " ":
                self.reverse(chars, start, end - 1)
                start = end + 1

        return "".join(chars)

    def remove_extra_spaces(self, chars: List[str]) -> int:
        fast = slow = 0

        while fast < len(chars) and chars[fast] == " ":
            fast += 1

        while fast < len(chars):
            if chars[fast] != " ":
                chars[slow] = chars[fast]
                slow += 1
            elif slow > 0 and chars[slow - 1] != " ":
                chars[slow] = " "
                slow += 1
            fast += 1

        if slow > 0 and chars[slow - 1] == " ":
            slow -= 1

        return slow

    def reverse(self, chars: List[str], left: int, right: int) -> None:
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
```

## 一句话总结

这道题的关键是：

**先用双指针把空格格式整理好，再整体反转字符串，最后逐个反转单词，从而得到单词顺序颠倒且空格规范的结果。**
