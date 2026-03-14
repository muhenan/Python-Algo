from typing import List

"""
猜测的 Wayfair 的面试题和算法，但实际并不是，留作纪念
"""

class TripPlan:
    @classmethod
    def giveMEAPlan(self, bigs, smalls):
        print(bigs, smalls)
    def move(self, num_big, num_small, weight_big, weight_small, big_trunk, small_trunk):
        trips = 0
        while num_big > 0 or num_small > 0:
            current_big_trunk = big_trunk
            current_small_trunk = small_trunk
            trips += 1
            while num_small > 0 and current_big_trunk >= weight_small:
                num_small -= 1
                current_big_trunk -= weight_small
            while num_small > 0 and current_small_trunk >= weight_small:
                num_small -= 1
                current_small_trunk -= weight_small
            while num_big > 0 and current_big_trunk >= weight_big:
                num_big -= 1
                current_big_trunk -= weight_big
            while num_big > 0 and current_small_trunk >= weight_big:
                num_big -= 1
                current_small_trunk -= weight_big
        return trips

    def hop(self, a, f):
        return 0 if a[f] == f else 1 + self.hop(a, a[f])


TripPlan.giveMEAPlan(34, 67)

tp = TripPlan()

print(tp.move(1,2,6,4,10,4))


"""

4 large -> 6
8 small -> 2

Trunk small -> 10
Trunk big -> 15


4 4
6

10
4

"""
