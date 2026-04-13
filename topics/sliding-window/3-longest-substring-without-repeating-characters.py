"""
LeetCode 3: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3  ("abc")

Example 2:
    Input: s = "bbbbb"
    Output: 1  ("b")

Example 3:
    Input: s = "pwwkew"
    Output: 3  ("wke")

Constraints:
    0 <= s.length <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.

Tags:
- Hash Table
- String
- Sliding Window
"""


def max_substring(s):
    """
    方法一：计数窗口
    char_map 记录窗口内每个字符的出现次数，右指针遇到重复字符时收缩左边。
    """
    char_map = {}
    left = 0
    ans = 0

    for right in range(len(s)):
        # 如果右指针字符已经在窗口里，收缩左边直到没有重复
        if s[right] in char_map and char_map[s[right]] > 0:
            while char_map[s[right]] > 0:
                char_map[s[left]] -= 1
                left += 1

        char_map[s[right]] = char_map.get(s[right], 0) + 1
        ans = max(ans, right - left + 1)

    return ans


def max_substring2(s):
    """
    方法二：记录上次出现位置（更简洁）
    last_seen 记录每个字符上次出现的 index，
    遇到重复时直接把 left 跳到重复字符的下一位，O(n) 无内层循环。
    """
    last_seen = {}  # char -> 上次出现的 index
    left = 0
    ans = 0

    for right in range(len(s)):
        if s[right] in last_seen and last_seen[s[right]] >= left:
            # 直接把 left 跳到重复字符的下一位
            left = last_seen[s[right]] + 1

        last_seen[s[right]] = right
        ans = max(ans, right - left + 1)

    return ans


def max_substring3(s):
    """
    方法三：set 窗口（最好写、最好记）
    用 set 判断重复，收缩时直接 remove，不需要维护计数。
    by 阶跃星辰 (StepFun)
    """
    char_set = set()
    left = ans = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        ans = max(ans, right - left + 1)
    return ans


# Tests
if __name__ == "__main__":
    for fn in [max_substring, max_substring2, max_substring3]:
        assert fn("abcabcbb") == 3
        assert fn("bbbbb") == 1
        assert fn("pwwkew") == 3
        assert fn("abcaf") == 4
        assert fn("aaa") == 1
        assert fn("") == 0

    print("All tests passed!")
