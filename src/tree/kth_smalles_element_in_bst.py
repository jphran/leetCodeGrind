"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
"""
# Definition for a binary tree node.
import sys
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack: list[TreeNode] = []
        stack.append(root)

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

            if len(stack) == 0 and root is None:
                break

        return sys.maxsize


# WORKING RECURSIVE
# class Solution:
#     def _recursive_inorder_traversal(
#         self, smallest: list[int], node: TreeNode
#     ) -> list[int]:
#         if node is None:
#             return []
#         self._recursive_inorder_traversal(smallest, node.left)
#         smallest.append(node.val)
#         self._recursive_inorder_traversal(smallest, node.right)
#         return smallest
#
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         smallest: list[int] = []
#         smallest = self._recursive_inorder_traversal(smallest, root)
#         return smallest[k - 1]
