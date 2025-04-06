from typing import List, Optional
import heapq

class ListNode:
    """链表节点的定义"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeKSortedLists:
    """
    LeetCode 23: Merge k Sorted Lists
    
    Problem Description:
    给定 k 个升序链表，将所有链表合并为一个升序链表并返回。
    
    Examples:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    
    提供四种解法：
    1. 顺序合并：反复调用合并两个链表
    2. 分治合并：递归地将链表分组合并
    3. 优先队列（值）：将所有值放入堆中
    4. 优先队列（节点）：将节点放入堆中
    """
    
    def mergeTwo(self, list1, list2):
        """
        基础方法：合并两个有序链表
        Time: O(n + m), Space: O(1)
        """
        dummy = ListNode(-1)
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next
            
        # 处理剩余节点
        if list1: curr.next = list1
        if list2: curr.next = list2
        return dummy.next

    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        方法一：顺序合并
        Time: O(k²n) - k个链表，每个长度约为n
        Space: O(1)
        
        思路：逐个合并链表，每次合并两个
        缺点：每个节点会被重复处理多次
        """
        answer = None
        for head in lists:
            answer = self.mergeTwo(answer, head)
        return answer

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        方法二：分治合并
        Time: O(kn * logk) - 递归树高度为logk
        Space: O(logk) - 递归栈深度
        
        思路：将链表两两分组，递归合并
        优点：每个节点在每一层只被处理一次
        """
        length = len(lists)
        if length == 0: return None
        if length == 1: return lists[0]
        mid = length // 2
        list1 = self.mergeKLists2(lists[:mid])
        list2 = self.mergeKLists2(lists[mid:])
        return self.mergeTwo(list1, list2)

    def mergeKLists3(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        方法三：优先队列（存储值）
        Time: O(nk * log(nk)) - nk个节点入堆
        Space: O(nk) - 需要存储所有节点值
        
        思路：将所有值放入最小堆中，再构建新链表
        优点：实现简单，实际运行较快
        缺点：空间复杂度较高
        """
        dummy = ListNode(-1)
        curr = dummy
        heap = []
        
        # 将所有值加入堆
        for head in lists:
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
                
        # 从堆中依次取出最小值构建链表
        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
        return dummy.next

    def mergeKLists4(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        方法四：优先队列（存储节点）
        Time: O(nk * logk) - 每个节点只入堆一次
        Space: O(k) - 堆中最多k个节点
        
        思路：将k个链表的头节点放入堆中，每次取出最小的
        优点：空间效率最优，不需要复制节点
        """
        # 定义节点比较规则
        ListNode.__lt__ = lambda A, B: A.val < B.val
        
        dummy = ListNode(-1)
        curr = dummy
        heap = []
        
        # 将所有头节点加入堆
        for head in lists:
            if head: heapq.heappush(heap, head)
            
        # 不断从堆中取出最小节点
        while heap:
            node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, node.next)
                
        return dummy.next 