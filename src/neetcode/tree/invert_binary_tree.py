"""
Given the root of a binary tree, invert the tree, and return its root.

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root

        # WORKING ITERATIVE SOLN
        # if root is None:
        #     return root
        #
        # q: deque[TreeNode] = deque()
        # q.append(root)
        #
        # while len(q) > 0:
        #     curr = q.pop()
        #
        #     if curr.right is not None:
        #         q.append(curr.right)
        #     if curr.left is not None:
        #         q.append(curr.left)
        #
        #     curr.left, curr.right = curr.right, curr.left
        #
        # return root
