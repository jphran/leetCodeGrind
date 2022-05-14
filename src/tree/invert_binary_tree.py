"""
Given the root of a binary tree, invert the tree, and return its root.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _recursive_dfs_inversion(self, node: TreeNode) -> None:
        """
        flips left and right nodes, then recursively dfs
        :param node:
        :return:
        """
        if node is None:
            return

        self.invertTree(node.left)
        self.invertTree(node.right)

        tmp_left = node.left
        node.left = node.right
        node.right = tmp_left

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self._recursive_dfs_inversion(root)

        return root