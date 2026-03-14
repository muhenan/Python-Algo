from typing import List


class CircularSentenceChecker:
    """
    LeetCode 2490: Circular Sentence (Weekly Contest 322)
    
    A sentence is circular if:
    - The last character of each word is equal to the first character of the next word
    - The last character of the last word is equal to the first character of the first word
    
    Example:
    Input: sentence = "leetcode exercises sound delightful"
    Output: true
    Explanation: The words in sentence are ["leetcode","exercises","sound","delightful"]:
    - leetcode's last char = exercises's first char
    - exercises's last char = sound's first char
    - sound's last char = delightful's first char
    - delightful's last char = leetcode's first char
    
    Tags:
    - String
    - Array
    - Word Processing
    
    Time Complexity: O(n) where n is length of sentence
    Space Complexity: O(n) for storing words array
    """
    def isCircularSentence(self, sentence: str) -> bool:
        """
        Check if a sentence is circular based on word characters
        
        Args:
            sentence: String containing space-separated words
            
        Returns:
            bool: True if sentence is circular, False otherwise
            
        Strategy:
            - Split sentence into words
            - Check adjacent words for character matching
            - Check first and last words for circular property
        """
        words = sentence.split(' ')
        # Check adjacent words
        for i in range(len(words) - 1):
            if words[i][-1] != words[i+1][0]:
                return False
        # Check circular property (first word's start matches last word's end)
        return words[0][0] == words[-1][-1]
