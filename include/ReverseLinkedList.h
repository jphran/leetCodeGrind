//Given the head of a singly linked list, reverse the list, and return the reversed list.
//
// Created by jfrancis on 4/15/21.
//

#ifndef LEETCODEGRIND_REVERSELINKEDLIST_H
#define LEETCODEGRIND_REVERSELINKEDLIST_H

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    explicit ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}

    std::vector<int> toArray() {
        std::vector<int> result{};
        ListNode *tmp = nullptr;
        if(this && this->next) {
            tmp = this;
            while (tmp->next) {
                result.emplace_back(tmp->val);
                tmp = tmp->next;
            }
            result.emplace_back(tmp->val);
        }
        return result;
    }
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* currNode = head;
        ListNode* nextNode = nullptr;
        ListNode* prevNode = nullptr;
        if(head) {
            while (currNode->next) {
                // reverse
                nextNode = currNode->next;
                currNode->next = prevNode;
                // setup for next iteration
                prevNode = currNode;
                currNode = nextNode;
            }
            currNode->next = prevNode;
        }
        return currNode;
    }
};
#endif //LEETCODEGRIND_REVERSELINKEDLIST_H
