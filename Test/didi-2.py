'''

+-*/()

s = '4+8'
ture

s = '(4*3)'
ture

(4+3)*14

16

(()(()))
'''
from collections import deque


class Solution:
    def is_valid(self, s):


        # operand
        for i in range(0, len(s)):
            if s[i] in ('+', '-', '*', '/'):
                if i == 0 or i == len(s) - 1:
                    return False
                if s[i - 1] in ('(', ')', '+', '-', '*', '/') or s[i + 1] in ('(', ')', '+', '-', '*', '/'):
                    return False


        # ()
        my_stack = deque()
        for c in s:
            if c in ('(', ')'):
                my_stack.append(c)



        index = 0
        left = 0
        '())('
        while index < len(my_stack):
            if s[index] == '(':
                left += 1
            else:
                left -= 1
                if left < 0:
                    return False
            index += 1
        if left != 0:
            return False
# [-,+]
#$

        return True