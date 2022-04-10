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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(val=69)

        curr_node = head
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                curr_node.next = list1
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next
            curr_node = curr_node.next

        if list1 is not None:
            curr_node.next = list1
        if list2 is not None:
            curr_node.next = list2

        return head.next


if __name__ == "__main__":
    s = Solution()
    one = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4)))
    two = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))
    result = s.mergeTwoLists(one, two)
    while result:
        print(result.val)
        result = result.next
