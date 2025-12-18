from typing import Optional
from ListNode import ListNode

class Solution:

    def swap_adjacent(self, pre: ListNode) -> None:
        node1 = pre.next
        node2 = node1.next
        post = node2.next
        # pre, node1, node2, post

        # 把变量都保持下来之后，这里的顺序就无所谓了
        node1.next = post
        node2.next = node1
        pre.next = node2

    def swap_remote(self, pre1: ListNode, pre2: ListNode) -> None:
        node1 = pre1.next
        node2 = pre2.next
        post1 = node1.next
        post2 = node2.next
        # pre1, node1, post1
        # pre2, node2, post2

        # 把变量都保持下来之后，这里的顺序就无所谓了
        pre1.next = node2
        node2.next = post1
        pre2.next = node1
        node1.next = post2

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        # find pre_first and first
        pre_first = dummy
        for _ in range(k - 1):
            pre_first = pre_first.next
        first = pre_first.next

        # find pre_second and second
        pre_second = dummy
        fast = first
        while fast.next:
            pre_second = pre_second.next
            fast = fast.next
        second = pre_second.next

        # if first and second are the same node, return the head
        if first == second:
            return dummy.next

        # if first and second are adjacent, swap them
        if first.next == second:
            self.swap_adjacent(pre_first)
        # if second and first are adjacent, swap them
        elif second.next == first:
            self.swap_adjacent(pre_second)
        # if first and second are not adjacent, swap them
        else:
            self.swap_remote(pre_first, pre_second)

        return dummy.next