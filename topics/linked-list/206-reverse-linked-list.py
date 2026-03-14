from typing import Optional
from utils.ListNode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = pre
            pre = curr
            curr = next_node
        return pre