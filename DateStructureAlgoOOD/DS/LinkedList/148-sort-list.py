from typing import Optional
from ListNode import ListNode

"""
LeetCode 148: Sort List

不递归， 而是用迭代的方法，自底向上地合并链表
"""
class Solution:

    def _get_length(self, head: Optional[ListNode]) -> int:
        """计算链表长度"""
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def _merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> tuple:
        """合并两个有序链表，返回 (头, 尾)"""
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2

        while cur.next:
            cur = cur.next

        return dummy.next, cur

    def _split(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """从 head 开始切 n 个节点，返回剩余部分的头"""
        if not head:
            return None

        for _ in range(n - 1):
            if not head.next:
                return None
            head = head.next

        rest = head.next
        head.next = None
        return rest
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length = self._get_length(head)
        dummy = ListNode(next=head)
        step = 1

        while step < length:
            cur = dummy.next
            tail = dummy

            while cur:
                left = cur
                right = self._split(left, step)
                cur = self._split(right, step)

                merged_head, merged_tail = self._merge(left, right)
                tail.next = merged_head
                tail = merged_tail

            step *= 2

        return dummy.next


"""
递归的方法，自顶向下地合并链表

写起来很简单，但是需要额外空间，因为需要递归栈
时间复杂度：O(nlogn)
空间复杂度：O(logn)
"""
class Solution2:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 快慢指针找中点
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 这里快慢指针的逻辑，如果是起始的索引是1
        # 那么 slow 1, 2, 3
        #      fast 2, 4, 6
        # slow 永远是前一半的最后一个节点或者中点

        mid = slow.next # 这里如果链表长度是奇数，slow刚好是中点，则前一半的长度比后一半的长度多1
        slow.next = None

        # 递归 + 合并
        return self.merge(self.sortList(head), self.sortList(mid))

    def merge(self, l1, l2):
        dummy = cur = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next