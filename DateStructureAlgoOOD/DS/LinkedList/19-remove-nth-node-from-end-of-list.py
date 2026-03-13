from typing import Optional
from ListNode import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        pre_to_remove = dummy
        while fast:
            pre_to_remove = pre_to_remove.next
            fast = fast.next
        pre_to_remove.next = pre_to_remove.next.next
        return dummy.next