class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        length = len(s)
        for i in range(length):
            step = 0
            while i - step >= 0 and i + step < length:
                if s[i - step] == s[i + step]:
                    ans += 1
                    step += 1
                else:
                    break
        for i in range(length - 1):
            step = 0
            while i - step >= 0 and i + step + 1 < length:
                if s[i - step] == s[i + step + 1]:
                    ans += 1
                    step += 1
                else:
                    break
        return ans

    """
    Manacher's Algorithm 马拉车算法
    时间复杂度 O(n)
    空间复杂度 O(n)
    """
    def countSubstrings2(self, s: str) -> int:
        # 预处理：插入 #
        t = '#'.join('^{}$'.format(s))
        n = len(t)
        p = [0] * n  # p[i] 表示以 i 为中心的回文半径
        center = right = 0

        for i in range(1, n - 1):
            # 利用对称性初始化
            if i < right:
                p[i] = min(right - i, p[2 * center - i]) # 找到对称点的回文半径，但不能大于 right - i，因为 right 是当前最右边界

            # 尝试扩展
            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1

            # 更新最右边界
            if i + p[i] > right:
                center, right = i, i + p[i]

        return sum((v + 1) // 2 for v in p)