from typing import List


class Solution:
    def vowelStrings1(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        isVowel = [False] * len(words)
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                isVowel[i] = True
        res = []
        for q in queries:
            temp = 0
            for i in range(q[0], q[-1] + 1):
                if isVowel[i]:
                    temp += 1
            res.append(temp)
        return res
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        prefixSum = [0]
        for i, word in enumerate(words):
            prefixSum.append(prefixSum[-1] + ( 1 if word[0] in vowels and word[-1] in vowels else 0))
        res = []
        for q in queries:
            res.append(prefixSum[q[-1] + 1] - prefixSum[q[0]])
        return res

        # prefixSum = [0]
        # for word in words:
        #     prefixSum.append(prefixSum[-1] + int(word[0] in "aeiou" and word[-1] in "aeiou"))
        # return [prefixSum[q[1] + 1] - prefixSum[q[0]] for q in queries]


solu = Solution()
print(solu.vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]))