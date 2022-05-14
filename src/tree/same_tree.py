"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # NOTE: could just simply do dfs or bfs with both nodes and compare at each node, but to make it more fun i'm going to try a topological sort
    def _pre_order_topo_sort(self, node: TreeNode, sorted: list[Optional[int]]) -> list[int]:
        sorted.append(node.val)
        if node.left:
            self._pre_order_topo_sort(node.left, sorted)
        else:
            sorted.append(None)
        if node.right:
            self._pre_order_topo_sort(node.right, sorted)
        else:
            sorted.append(None)

        return sorted

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        sorted_p: list[Optional[int]] = []
        sorted_p = self._pre_order_topo_sort(p, sorted_p)
        sorted_q: list[Optional[int]] = []
        sorted_q = self._pre_order_topo_sort(q, sorted_q)

        return sorted_p == sorted_q