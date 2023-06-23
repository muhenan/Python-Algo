class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or len(t) == 0:
            return ""

        need = {}
        for c in t:
            if c not in need:
                need[c] = 0
            need[c] -= 1

        diff = len(need)


        left = -1 # 我的习惯是 left 是开的
        minLength = len(s) + 1
        minLeft, minRight = 0, 0

        for i, c in enumerate(s):
            if c in need:
                need[c] += 1
                if need[c] == 0:
                    diff -= 1
            while diff == 0:
                if i - left < minLength:
                    minLength = i - left
                    minLeft = left
                    minRight = i
                left += 1
                if s[left] in need:
                    need[s[left]] -= 1
                    if need[s[left]] == -1:
                        diff += 1

        return s[minLeft + 1:minRight + 1] if minLength < len(s) + 1 else ""
