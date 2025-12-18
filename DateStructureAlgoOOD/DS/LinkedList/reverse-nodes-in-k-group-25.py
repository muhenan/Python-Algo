from typing import Optional
from ListNode import ListNode

class Solution:
    
    def _reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = pre
            pre = curr
            curr = next_node
        return pre

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        # 找到一组的最后一个节点，并且把这一组断开
        tail = head
        for _ in range(k - 1):
            if tail.next is None: # 如果这一组的长度小于 k，则直接返回原链表
                return head
            tail = tail.next
        
        next_head = tail.next # 保存下一组的头节点
        tail.next = None # 把这一组断开

        # 反转这一组，反转之后，head 是这一组的最后一个节点，tail 是这一组的第一个节点
        self._reverseList(head)

        # 递归反转下一组
        head.next = self.reverseKGroup(next_head, k)
        return tail