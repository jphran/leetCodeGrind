//Given the root of a binary tree, return its maximum depth.
//A binary tree's maximum depth is the number of nodes along
//the longest path from the root node down to the farthest leaf node.
//
// Created by jfrancis on 4/21/21.
//

#ifndef LEETCODEGRIND_MAXIMUMDEPTHOFBINARYTREE_H
#define LEETCODEGRIND_MAXIMUMDEPTHOFBINARYTREE_H


//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(not root)
            return 0;

        return depthFirstSearch(root);
    }

private:
    int depthFirstSearch(TreeNode* node) {
        if(not node) {
            return 0;
        }

        int leftDepth = depthFirstSearch(node->left);
        int rightDepth = depthFirstSearch(node->right);

        return std::max(leftDepth, rightDepth) + 1;
    }
};

#endif //LEETCODEGRIND_MAXIMUMDEPTHOFBINARYTREE_H
