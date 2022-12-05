from typing import List


class Solution6253:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        for i in range(len(words) - 1):
            if words[i][-1] != words[i+1][0]:
                return False
        return words[0][0] == words[-1][-1]

class Solution6254:
    def dividePlayers(self, skill: List[int]) -> int:
        # if len(skill) == 2:
        #     return skill[0]*skill[1]
        skill.sort()
        k = skill[0] + skill[-1]
        result = skill[0] * skill[-1]
        theLength = len(skill)
        for i in range(1, theLength//2):
            if skill[i] + skill[theLength - i - 1] != k:
                return -1
            else:
                result += skill[i] * skill[theLength - i - 1]
        return result
