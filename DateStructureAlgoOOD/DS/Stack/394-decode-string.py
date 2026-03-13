"""
LeetCode 394: Decode String
https://leetcode.com/problems/decode-string/

Problem Description:
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则是：k[encoded_string]，表示encoded_string重复k次。
注意：k保证为正整数。

Examples:
s = "3[a]2[bc]" -> "aaabcbc"
s = "3[a2[c]]" -> "accaccacc"
s = "2[abc]3[cd]ef" -> "abcabccdcdcdef"

Time Complexity: O(n), n为解码后的字符串长度
Space Complexity: O(m), m为编码字符串中嵌套的最大深度
"""

class DecodeString:
    def decodeString_stack(self, s: str) -> str:
        """
        栈方法：使用栈存储之前的状态
        """
        stack = []      # 存储之前的状态 [数字, 字符串]
        cur_str = ""    # 当前正在处理的字符串
        multi = 0       # 当前的数字
        
        for c in s:
            if c.isdigit():
                # 处理数字，可能是多位数
                multi = multi * 10 + int(c)
            elif c == '[':
                # 遇到左括号，保存当前状态并重置
                stack.append([multi, cur_str])
                cur_str, multi = "", 0
            elif c == ']':
                # 遇到右括号，弹出上一个状态并处理
                cur_multi, previous_str = stack.pop()
                # 将当前字符串重复指定次数，并加到之前的字符串后
                cur_str = previous_str + cur_multi * cur_str
            else:
                # 普通字符直接添加到当前字符串
                cur_str += c
                
        return cur_str

    def decodeString_recursive(self, s: str) -> str:
        """
        递归方法：使用DFS处理嵌套的括号结构
        """
        def dfs(s: str, i: int) -> tuple[str, int]:
            """
            递归处理字符串
            Args:
                s: 输入的编码字符串
                i: 当前处理的位置
            Returns:
                tuple[str, int]: (解码后的字符串, 结束位置)
            """
            current_str = ""  # 当前层的字符串
            multi = 0        # 当前的数字
            
            while i < len(s):
                if s[i].isdigit():
                    # 处理数字
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    # 递归处理括号内的内容
                    sub_str, i = dfs(s, i + 1)
                    # 将子串重复指定次数
                    current_str += multi * sub_str
                    multi = 0
                elif s[i] == ']':
                    return current_str, i
                else:
                    # 处理普通字符
                    current_str += s[i]
                i += 1
                
            return current_str, i

        return dfs(s, 0)[0]


# 测试代码
def test_decode_string():
    solution = DecodeString()
    
    # 测试用例
    test_cases = [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("abc3[cd]xyz", "abccdcdcdxyz"),
    ]
    
    for s, expected in test_cases:
        assert solution.decodeString_recursive(s) == expected
        assert solution.decodeString_stack(s) == expected
        print(f"Test case passed: {s} -> {expected}")

if __name__ == "__main__":
    test_decode_string() 