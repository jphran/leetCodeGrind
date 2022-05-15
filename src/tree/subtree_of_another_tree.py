"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of
root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this
node's descendants. The tree tree could also be considered as a subtree of itself.

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _recursive_is_subtree(self, tree: TreeNode, sub_tree: TreeNode) -> bool:
        # base case, reached a nonetype leaf
        if tree and sub_tree:
            return (
                tree.val == sub_tree.val
                and self._recursive_is_subtree(tree.left, sub_tree.left)
                and self._recursive_is_subtree(tree.right, sub_tree.right)
            )

        return tree is sub_tree

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self._recursive_is_subtree(root, subRoot):
            return True

        return self.isSubtree(
            root.left, subRoot
        ) or self.isSubtree(root.right, subRoot)
