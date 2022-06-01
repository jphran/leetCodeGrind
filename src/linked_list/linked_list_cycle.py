"""
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set: set[ListNode] = set()
        while head:
            if head in node_set:
                return True
            node_set.add(head)
            head = head.next

        return False


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)

    assert not s.hasCycle(head)

    head.next.next.next = head
    assert s.hasCycle(head)



# WORKING SOLN
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     visited = set()
    #     while head is not None:
    #         if head in visited:
    #             return True
    #         visited.add(head)
    #         head = head.next
    #     return False
