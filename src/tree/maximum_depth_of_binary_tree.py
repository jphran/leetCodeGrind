"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _recursive_depth_first_search(self, node: TreeNode) -> int:
        left_depth = 0
        right_depth = 0
        if node.left:
            left_depth = self._recursive_depth_first_search(node.left)
        if node.right:
            right_depth = self._recursive_depth_first_search(node.right)

        return max(left_depth, right_depth) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._recursive_depth_first_search(root) if root else 0
