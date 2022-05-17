"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _is_sub_tree_valid_bst(self, node: TreeNode, min_val: int, max_val) -> bool:
        if node is None:
            return True
        if node.val >= max_val or node.val <= min_val:
            return False

        return self._is_sub_tree_valid_bst(
            node.left, min_val, node.val
        ) and self._is_sub_tree_valid_bst(node.right, node.val, max_val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._is_sub_tree_valid_bst(root, -sys.maxsize, sys.maxsize)
