# class WordDictionary:
#
#     def __init__(self):
#         self.words = []
#
#     def addWord(self, word: str) -> None:
#         self.words.append(word)
#
#     def search(self, word: str) -> bool:
#         for curr_word in self.words:
#             if len(word) != len(curr_word):
#                 continue
#             for i in range(len(word)):
#                 if word[i] != "." and word[i] != curr_word[i]:
#                     break
#                 if i == len(word) - 1:
#                     return True
#         return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# dad d.d


class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    def insert(self, word : str) -> None:
        curr_node = self
        for char in word:
            if char not in curr_node:
                curr_node[char] = Trie()
            curr_node = curr_node[char]
        curr_node.isEnd = True


class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        def dfs(index: int, node : Trie) -> bool:
            if index == len(word):
                return True
            char = word[index]
            if char != '.':
                if char not in node.children:
                    return False
                return dfs(index + 1, node.children[char])
            else:
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
            return False
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# dad d.d