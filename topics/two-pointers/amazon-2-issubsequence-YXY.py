"""
题目要求：
给定两个字符串 `longerStr` 和 `shorterStr`。

我们可以从 `longerStr` 中按顺序选择若干字符，来匹配 `shorterStr`。
这里每个被选中的字符有两种用法：

1. 直接使用它本身
2. 把它“向后循环变换一个字符”后再使用
   - 例如 `a -> b`
   - `b -> c`
   - ...
   - `y -> z`
   - `z -> a`

问：是否可以通过这种方式，使 `shorterStr` 成为 `longerStr` 的一个子序列。

注意：
- 子序列要求保持相对顺序不变
- 不要求连续
- `longerStr` 中的每个字符最多使用一次
- 每个字符至多做一次“向后循环变换一个字符”


例子理解：

例 1：
longerStr = "xasd", shorterStr = "be"

匹配过程可以是：
- longerStr[1] = 'a'，变成 'b'，匹配 shorterStr[0] = 'b'
- longerStr[3] = 'd'，变成 'e'，匹配 shorterStr[1] = 'e'

顺序满足，所以返回 True。


做题思路：
这题的核心是：双指针 + 贪心。

为什么可以贪心？
因为我们从左到右扫描 `longerStr` 时，
只要当前字符能够匹配 `shorterStr[i_s]`，
就应该立刻拿它来匹配。

原因是：
- 子序列问题只关心“顺序”，不关心必须连续
- 越早匹配当前目标字符，给后面的字符留下的选择空间越大
- 如果当前能匹配却故意跳过，不会让后面更优

所以贪心策略是：
- `i_l` 指向 `longerStr`
- `i_s` 指向 `shorterStr`
- 如果 `longerStr[i_l]` 本身就等于 `shorterStr[i_s]`
  或者 `longerStr[i_l]` 变换一次后等于 `shorterStr[i_s]`
  那么就让这两个字符匹配，两个指针都向右走
- 否则只能跳过 `longerStr[i_l]`，让 `i_l` 向右走

最后如果 `i_s` 走到了 `shorterStr` 末尾，
说明 `shorterStr` 的所有字符都成功匹配，返回 True；
否则返回 False。


为什么 `nextChar()` 要单独处理 `z`？
因为题目要求是“循环变换”：
- `a -> b`
- ...
- `z -> a`

所以：
- 如果当前字符是 `z`，下一个字符应该回到 `a`
- 其他字符直接用 ASCII/Unicode 编码加一即可


时间复杂度：
- O(n)，其中 n 是 `longerStr` 的长度

空间复杂度：
- O(1)
"""
def isSubSequence(longerStr : str, shorterStr : str) -> bool:
    def nextChar(c : str):
        if c == 'z':
            return 'a'
        return chr(ord(c) + 1)
    n_long, n_short = len(longerStr), len(shorterStr)
    if n_long < n_short:
        return False
    i_l, i_s = 0, 0
    while i_l < n_long and i_s < n_short:
        if longerStr[i_l] == shorterStr[i_s] or nextChar(longerStr[i_l]) == shorterStr[i_s]:
            i_l += 1
            i_s += 1
        else:
            i_l += 1
    return i_s == n_short

print(isSubSequence("xasd", "be"))
print(isSubSequence("sdfasd", "ege"))
print(isSubSequence("xasd", "we"))