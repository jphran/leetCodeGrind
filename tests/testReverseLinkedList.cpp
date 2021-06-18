//
// Created by jfrancis on 4/15/21.
//

#define CATCH_CONFIG_MAIN

#include <catch2/catch.hpp>
#include "linked_list/ReverseLinkedList.h"
#include <iostream>

//********************TWO SUM*************************
TEST_CASE("Given the head of a singly linked list, reverse the list, and return the reversed list."
, "[ReverseLinkedList]") {
    ListNode* head;
    ListNode* tail;
    int n = 3;
    for(int i = 1; i <= n; ++i) {
        auto newNode = new ListNode(i);
        if(i == 1) {
            head = newNode;
            tail = newNode;
        }
        else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    ListNode* ansHead;
    ListNode* ansTail;
    for(int i = n; i >= 1; --i) {
        auto newNode = new ListNode(i);
        if(i == n) {
            ansHead = newNode;
            ansTail = newNode;
        }
        else {
            ansTail->next = newNode;
            ansTail = newNode;
        }
    }

    Solution s;

    REQUIRE(s.reverseList(head)->toArray() == ansHead->toArray());
}

TEST_CASE("Given the head of a singly linked list, reverse the list, and return the reversed list1."
, "[ReverseLinkedList]") {
    ListNode* head;
    ListNode* tail;
    int n = 1;
    for(int i = 1; i <= n; ++i) {
        auto newNode = new ListNode(i);
        if(i == 1) {
            head = newNode;
            tail = newNode;
        }
        else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    ListNode* ansHead;
    ListNode* ansTail;
    for(int i = n; i >= 1; --i) {
        auto newNode = new ListNode(i);
        if(i == n) {
            ansHead = newNode;
            ansTail = newNode;
        }
        else {
            ansTail->next = newNode;
            ansTail = newNode;
        }
    }

    Solution s;

    REQUIRE(s.reverseList(head)->toArray() == ansHead->toArray());
}

TEST_CASE("Given the head of a singly linked list, reverse the list, and return the reversed list2."
, "[ReverseLinkedList]") {
    ListNode* head;
    ListNode* tail;
    int n = 10;
    for(int i = 1; i <= n; ++i) {
        auto newNode = new ListNode(i);
        if(i == 1) {
            head = newNode;
            tail = newNode;
        }
        else {
            tail->next = newNode;
            tail = newNode;
        }
    }

    ListNode* ansHead;
    ListNode* ansTail;
    for(int i = n; i >= 1; --i) {
        auto newNode = new ListNode(i);
        if(i == n) {
            ansHead = newNode;
            ansTail = newNode;
        }
        else {
            ansTail->next = newNode;
            ansTail = newNode;
        }
    }

    Solution s;

    REQUIRE(s.reverseList(head)->toArray() == ansHead->toArray());
}

TEST_CASE("Given the head of a singly linked list, reverse the list, and return the reversed list3."
, "[ReverseLinkedList]") {
    ListNode* head = nullptr;
    Solution s;
    REQUIRE(s.reverseList(head)->toArray() == head->toArray());
}