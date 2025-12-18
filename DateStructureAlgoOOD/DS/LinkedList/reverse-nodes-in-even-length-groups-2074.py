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

    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre_first = dummy # pre_first will never be None, it's always the last node of the previous group
        length = 0
        while True:
            if pre_first.next is None: # if pre_first is the last node of the list, break
                return dummy.next
            length += 1
            first = pre_first.next

            # find the last node of the current group
            second = first
            current_length = 1
            for _ in range(length - 1):
                if second.next is None:
                    break
                current_length += 1
                second = second.next
            
            # get the min length of the current group if it is less than length
            min_length = min(length, current_length)
            
            if min_length % 2 == 0: # if the length of the current group is even, reverse it
                after_second = second.next # save the next node of the last node of the current group
                second.next = None
                pre_first.next = None # break the current group
                self._reverseList(first) # reverse the current group
                first.next = after_second # connect the reversed group to the next group
                pre_first.next = second # connect the last node of the previous group to the first node of the current group
                pre_first = first # move the pre_first to the last node of the current group
            else: # if the length of the current group is odd, move the pre_first to the last node of the current group
                pre_first = second