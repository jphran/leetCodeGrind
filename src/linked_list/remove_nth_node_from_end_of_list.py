"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and head.next is None:
            return None

        curr_node = head
        node_before_removal = None
        i = 0

        # find nth node from the end
        while curr_node:
            if i == n:
                node_before_removal = head
            elif i > n:
                node_before_removal = node_before_removal.next
            i += 1
            curr_node = curr_node.next

        # remove that bad boy
        if node_before_removal is not None:
            node_before_removal.next = node_before_removal.next.next
        else:
            head = head.next

        return head


if __name__ == "__main__":
    s = Solution()
    h = ListNode(
        val=1,
        next=ListNode(
            val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))
        ),
    )
    result = s.removeNthFromEnd(h, 2)
    while result:
        print(result.val)
        result = result.next
