import collections


class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.deque = collections.deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.deque.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """

        while self.deque and timestamp - self.deque[0] >= 300: # 双端队列，最简单的解决问题的代码
            self.deque.popleft()
        return len(self.deque)