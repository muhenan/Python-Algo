from typing import Optional
from ListNode import ListNode

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        dummy = ListNode(next=head)
        
        first = dummy.next
        pre = dummy
        
        while first and first.next:
            # 宁愿多写几个变量，避免顺序的麻烦
            second = first.next
            post_second = second.next

            # 这里的顺序无所谓，因为已经把变量都保存下来了
            pre.next = second
            second.next = first
            first.next = post_second

            # 移动 pre 和 first 到下一对节点
            pre = first
            first = post_second
        return dummy.next