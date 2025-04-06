import collections


class HitCounterDesign:
    """
    LeetCode 362: Design Hit Counter
    
    Design a hit counter which counts the number of hits received in the past 5 minutes 
    (300 seconds). Each function accepts a timestamp parameter (in seconds granularity).
    
    Methods to implement:
    1. hit(timestamp): Records a hit at the given timestamp
    2. getHits(timestamp): Returns the number of hits in the past 5 minutes
    
    Example:
    HitCounter counter = new HitCounter();
    counter.hit(1);         // hit at timestamp 1
    counter.hit(2);         // hit at timestamp 2
    counter.getHits(3);     // get hits at timestamp 3, returns 2
    counter.hit(300);       // hit at timestamp 300
    counter.getHits(300);   // get hits at timestamp 300, returns 3
    counter.getHits(301);   // get hits at timestamp 301, returns 2
    
    Tags:
    - Design
    - Queue
    - Deque
    - Data Stream
    
    Time Complexity: 
    - hit: O(1)
    - getHits: O(n) worst case, but amortized O(1)
    Space Complexity: O(n), where n is number of hits in 5-minute window
    """

    def __init__(self):
        """
        Initialize hit counter using a deque to store timestamps
        The deque will maintain hits within the 5-minute window
        """
        self.hits_queue = collections.deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit at the given timestamp
        
        Args:
            timestamp: Current timestamp in seconds
            
        Strategy:
            - Simply append the timestamp to deque
            - Cleanup of old hits is handled in getHits
            
        Time Complexity: O(1)
        Space Complexity: O(1) per hit
        """
        self.hits_queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return number of hits in past 5 minutes (300 seconds)
        
        Args:
            timestamp: Current timestamp in seconds
            
        Returns:
            int: Number of hits in past 5 minutes
            
        Strategy:
            - Remove all hits older than 5 minutes from front of deque
            - Remaining hits in deque are within 5-minute window
            
        Time Complexity: O(n) worst case, but amortized O(1)
        Space Complexity: O(1)
        """
        while self.hits_queue and timestamp - self.hits_queue[0] >= 300:
            self.hits_queue.popleft()
        return len(self.hits_queue)