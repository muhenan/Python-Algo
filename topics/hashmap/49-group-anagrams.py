"""
LeetCode 49: Group Anagrams

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

Constraints:
    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

Tags:
- Array
- Hash Table
- String
- Sorting
"""

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d[tuple(s.count(c) for c in 'abcdefghijklmnopqrstuvwxyz')].append(s)
        return list(d.values())


# Tests
if __name__ == "__main__":
    s = Solution()

    assert sorted([sorted(g) for g in s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])]) == sorted([sorted(g) for g in [["bat"],["nat","tan"],["ate","eat","tea"]]])
    assert s.groupAnagrams([""]) == [[""]]
    assert s.groupAnagrams(["a"]) == [["a"]]

    print("All tests passed!")
