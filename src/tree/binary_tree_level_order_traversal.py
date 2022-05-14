"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result: list[list[[int]]] = []
        q = deque()
        q.append(root)
        while len(q) > 0:
            level = []
            for i in range(len(q)):
                node: TreeNode = q.pop()
                level.append(node.val)

                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)

            result.append(level)

        return result
