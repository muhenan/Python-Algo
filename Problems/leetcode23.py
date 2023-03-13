from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    """
    最简单的 merge two
    生成一个新 linkedlist
    也可以在原来的 list 上操作，打乱顺序，重新连起来
    """
    def mergeTwo(self, list1, list2):
        dummy = ListNode(-1)
        iteratePointer = dummy
        while list1 and list2:
            if list1.val < list2.val:
                iteratePointer.next = ListNode(list1.val)
                list1 = list1.next
            else:
                iteratePointer.next = ListNode(list2.val)
                list2 = list2.next
            iteratePointer = iteratePointer.next
        if list1: iteratePointer.next = list1
        if list2: iteratePointer.next = list2
        return dummy.next

    """
    method 1
    不断调用merge two
    time:
    最长的 list 是 n
    merge 一次平均的时间复杂度是 O(n * (k/2))
    merge k 次
    时间复杂度 O(k) * O(n * (k/2)) = O(k * k * n)
    所有 kn 都被使用了 k/2 次
    """
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # method 1
        answer = None
        for head in lists:
            answer = self.mergeTwo(answer, head)
        return answer

    """
    method 2
    所有 kn 都被使用了 logk 次
    time O(logk * k * n)
    """
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length = len(lists)
        if length == 0: return None
        if length == 1: return lists[0]
        mid = length // 2
        list1 = self.mergeKLists(lists[:mid])
        list2 = self.mergeKLists(lists[mid:])
        return self.mergeTwo(list1, list2)

    """
    method 3
    PQ / heap
    python 的最直接的优先队列方法，相当于把所有的都放进去排序了
    这样的话，时间复杂度是不如分治的
    时间复杂度是
    O(nklog(nk))
    但是实际跑起来是非常快的，有时候，真正运行的速度不知和时间复杂度有关，也和代码具体的写法有关
    """
    def mergeKLists3(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        iterateNode = dummy
        myHeap = []
        heapq.heapify(myHeap)
        for head in lists:
            while head:
                heapq.heappush(myHeap, head.val)
                head = head.next
        while myHeap:
            iterateNode.next = ListNode(heapq.heappop(myHeap))
            iterateNode = iterateNode.next
        return dummy.next

    """
    method 4
    和 Java 的优先队列的方法一样
    这里是直接把 ListNode 丢进 pq
    所以需要我们自己定义了 ListNode类 的比较规则（定义了一个小于）
    注意这里 __lt__ 的写法，直接就是 mergeKLists 中的一个子函数
    并不是 solution 的 self 函数
    所以直接在 mergeKLists 用 __lt__ 名字调用这个函数即可
    """
    def mergeKLists4(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # def __lt__(self, other):
        #     return self.val < other.val
        # ListNode.__lt__ = __lt__
        ListNode.__lt__ = lambda A, B: A.val < B.val
        dummy = ListNode(-1)
        iterateNode = dummy
        myHeap = []
        heapq.heapify(myHeap)
        for i in lists:
            if i :heapq.heappush(myHeap, i)
        while myHeap:
            node = heapq.heappop(myHeap)
            iterateNode.next = node
            iterateNode = iterateNode.next
            node = node.next
            if node: heapq.heappush(myHeap, node)
        return dummy.next