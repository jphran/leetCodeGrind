"""
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr: list[ListNode] = []
        curr_node = head
        while curr_node:
            arr.append(curr_node)
            curr_node = curr_node.next

        pre_insertion_idx = 0
        is_even = len(arr) % 2 == 0
        for i in range(len(arr) - 1, len(arr) // 2 - is_even, -1):
            arr[pre_insertion_idx].next = arr[i]
            pre_insertion_idx += 1
            arr[i].next = arr[pre_insertion_idx]

        arr[pre_insertion_idx].next = None

        return head


if __name__ == '__main__':
    s = Solution()
    h = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4))))  # , next=ListNode(val=5)))))
    s.reorderList(h)
    while h:
        print(h.val)
        h = h.next
