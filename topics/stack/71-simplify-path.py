"""
LeetCode 71: Simplify Path
https://leetcode.com/problems/simplify-path/
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = [] # 文件夹列表
        self.folder = '' # 当前的文件夹名
        self.pure_dot = True # 是否是纯点


        """
        处理单词：
        如果当前是纯点，则判断长度为2还是大于2
        如果不是纯电
            如果有文件名，则添加到文件夹列表
        """
        def handle_word():
            if self.pure_dot:
                length_dot = len(self.folder)
                if length_dot == 2:
                    if folders:
                        folders.pop()
                elif length_dot > 2:
                    folders.append(self.folder)
            elif self.folder:
                folders.append(self.folder)
            self.folder = ''
            self.pure_dot = True


        """
        遍历路径：
        如果当前是斜杠，则处理单词
        如果不是斜杠，则添加到当前文件夹名
        """
        for i in range(len(path)):
            if path[i] == '/':
                handle_word()
            else:
                self.folder += path[i]
                if path[i] != '.': # 如果当前不是点，则不是纯点
                    self.pure_dot = False

        """
        处理最后一个单词
        """
        handle_word()

        """
        如果文件夹列表为空，则返回根目录
        否则，则返回文件夹列表的拼接
        """
        if not folders:
            return '/'
        else:
            ans = ''
            for f in folders:
                ans += ('/' + f)
            return ans

solu = Solution()
print(solu.simplifyPath('/home/'))
print(solu.simplifyPath('/home//foo/'))
print(solu.simplifyPath('/home/user/Documents/../Pictures'))
print(solu.simplifyPath('/../'))
print(solu.simplifyPath('/.../a/../b/c/../d/./'))
print(solu.simplifyPath('/..hidden'))