from collections import deque
from typing import List


class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]: # if no, 1 prefer
        pre_one = -1
        current_time = 0
        current_index = 0
        current_count = 0
        n = len(arrival)
        result = [-1] * len(arrival)
        my_queue = [deque([]), deque([])]
        while current_count < n:
            while current_index < n and arrival[current_index] == current_time:
                my_queue[state[current_index]].append(current_index)
                current_index += 1
            if not my_queue[0] and not my_queue[1]:
                pre_one = -1
            elif my_queue[0] and my_queue[1]:
                if pre_one == -1:
                    pre_one = 1
                out_index = my_queue[pre_one].popleft()
                result[out_index] = current_time
                current_count += 1
            elif my_queue[0]:
                pre_one = 0
                out_index = my_queue[0].popleft()
                result[out_index] = current_time
                current_count += 1
            else:
                pre_one = 1
                out_index = my_queue[1].popleft()
                result[out_index] = current_time
                current_count += 1
            current_time += 1
        return result


solu = Solution()
solu.timeTaken([3,3,4,5,5,5], [1,0,1,0,1,0])