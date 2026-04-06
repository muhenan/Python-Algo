"""
LeetCode 187: Repeated DNA Sequences

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences
(substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:
    Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
    Input: s = "AAAAAAAAAAAAA"
    Output: ["AAAAAAAAAA"]

Constraints:
    1 <= s.length <= 10^5
    s[i] is either 'A', 'C', 'G', or 'T'

Tags:
- Hash Table
- String
- Sliding Window
- Rolling Hash
- Bit Manipulation

Hint: 长度固定为 10 的滑动窗口，关键在于如何高效判断窗口内字符串是否出现过。
      暴力做法：用 HashSet 存每个长度 10 的子串，O(10n) 空间。
      Rolling Hash：用数值表示窗口内容，滑动时 O(1) 更新，避免每次重新 hash 字符串。
"""

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        mp = {'A':0,'C':1,'G':2,'T':3}
        seen, ans = set(), set()
        h = 0
        for i, c in enumerate(s):
            h = (h * 4 + mp[c]) % (4**10)
            if i < 9:
                continue
            if h in seen:
                ans.add(s[i-9:i+1])
            seen.add(h)
        return list(ans)


# Tests
if __name__ == "__main__":
    sol = Solution()

    assert sorted(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) == sorted(["AAAAACCCCC", "CCCCCAAAAA"])
    assert sol.findRepeatedDnaSequences("AAAAAAAAAAAAA") == ["AAAAAAAAAA"]
    assert sol.findRepeatedDnaSequences("AAAAAAAAAA") == []
    assert sol.findRepeatedDnaSequences("AGTCAGTCAG") == []

    print("All tests passed!")
