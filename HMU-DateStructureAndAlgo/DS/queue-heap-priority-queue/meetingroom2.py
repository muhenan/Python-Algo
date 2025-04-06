import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x:x[0])
        q = [intervals[0][1]]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= q[0]:
                heapq.heappop(q)
            heapq.heappush(q, intervals[i][1])
        return len(q)

my_list = list()
my_list.append([3,2])
my_list.append([0,1])
print(my_list)

my_list.sort(key=lambda x:x[0])
print(my_list)

q = [4]
heapq.heappush(q, 6)
heapq.heappush(q, 3)

print(q[0])

heapq.heappop(q)

print(q[0])