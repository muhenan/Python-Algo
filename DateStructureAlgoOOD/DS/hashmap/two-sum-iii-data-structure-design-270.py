"""
LeetCode 270: Two Sum III - Data Structure Design
Given an integer array nums, design an algorithm to efficiently find a pair of values that sum to a given target number.
"""

class TwoSum:

    def __init__(self):
        self.arr_count = {}
    
    """
    Add the number to an internal data structure.
    Time: O(1)
    """
    def add(self, number: int) -> None:
        self.arr_count[number] = self.arr_count.get(number, 0) + 1

    """
    Find if there exists any pair of numbers which sum is equal to the value.
    Time: O(n)
    """
    def find(self, value: int) -> bool:
        for number, count in self.arr_count.items():
            target = value - number
            if target == number:
                if count > 1:
                    return True
            elif target in self.arr_count:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
obj.add(0)
param_2 = obj.find(0)
print(param_2)