from typing import Optional
from ListNode import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0, head)
        index = 1
        pre = dummy
        curr = head
        pre_left = None
        left_point = None
        while curr:
            if index < left:
                index += 1
                pre = curr
                curr = curr.next
            elif index == left:
                left_point = curr
                pre_left = pre
                index += 1
                pre = curr
                curr = curr.next
                left_point.next = None
            elif left < index < right:
                old_curr = curr # 这里保存当前节点，保存完之后 curr 指针就没用了，就可以马上往下走了
                curr = curr.next
                index += 1
                old_curr.next = pre # 这里先用 pre，用完了之后再往下走
                pre = old_curr
            elif index == right:
                after_right = curr.next
                curr.next = pre
                pre_left.next = curr
                left_point.next = after_right
                break
        return dummy.next

    """
    代码优化版本
    这种方法用了两个 for，但是思路更清晰，更容易理解
    """
    def reverseBetween2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 首先找到 left 节点的前一个节点
        pre_left = dummy = ListNode(next=head)
        for _ in range(left - 1):
            pre_left = pre_left.next

        # 这里最后找到的是
        # pre 是 right
        # cur 是 right 节点的下一个节点
        pre = None
        cur = pre_left.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre  # 每次循环只修改一个 next，方便大家理解
            pre = cur
            cur = nxt

        # 翻转完的链表的收尾处理一下
        pre_left.next.next = cur
        pre_left.next = pre
        return dummy.next