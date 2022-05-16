"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary
tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if len(preorder) <= 0 or len(inorder) <= 0:
            return None
        if len(inorder) == 1:
            preorder.pop(0)
            return TreeNode(inorder[0])

        root_val = preorder.pop(0)
        root_idx = inorder.index(root_val)
        root = TreeNode(val=root_val)
        root.left = self.buildTree(preorder, inorder[:root_idx])
        root.right = self.buildTree(preorder, inorder[root_idx + 1:])

        return root


if __name__ == '__main__':
    s = Solution()
    preorder = [1,2]
    inorder = [1,2]
    t = s.buildTree(preorder, inorder)
    print(t.val)