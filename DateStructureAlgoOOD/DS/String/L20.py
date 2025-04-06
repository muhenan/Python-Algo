class Solution:
    def isValid(self, s: str) -> bool:
        # stack
        dictionary = {
            '[': ']',
            '{': '}',
            '(': ')'
        }
        stack = []
        for c in s:
            if c in dictionary: # left
                stack.append(dictionary[c]) # put right one in stack
            else: # right
                if len(stack) == 0 or stack.pop() != c:
                    return False
        return len(stack) == 0
