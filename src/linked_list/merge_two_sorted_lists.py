"""
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is not None:
            return list2
        if list2 is None and list1 is not None:
            return list1
        if list1 is None and list2 is None:
            return None

        curr_node = None
        head = None

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                next_node = list1
                list1 = list1.next
            else:
                next_node = list2
                list2 = list2.next

            if curr_node is not None:
                curr_node.next = next_node
                curr_node = next_node
            else:
                curr_node = next_node
                head = next_node

        if list1 is not None:
            curr_node.next = list1
        if list2 is not None:
            curr_node.next = list2

        return head


if __name__ == '__main__':
    s = Solution()
    one = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4)))
    two = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))
    result = s.mergeTwoLists(one, two)
    while result:
        print(result.val)
        result = result.next
