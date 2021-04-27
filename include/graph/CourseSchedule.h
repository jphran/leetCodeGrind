//There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
//You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
// you must take course bi first if you want to take course ai.
//
//For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
//
//Return true if you can finish all courses. Otherwise, return false.

//
// Created by jfrancis on 4/23/21.
//

#ifndef LEETCODEGRIND_COURSESCHEDULE_H
#define LEETCODEGRIND_COURSESCHEDULE_H

#include <unordered_map>
#include <unordered_set>
#include <list>
#include <vector>
#include <queue>

class Solution {
public:
    bool canFinish(int numCourses, const std::vector<std::vector<int>>& prerequisites) {
        if(prerequisites.empty())
            return true;

        std::unordered_map<int, std::list<int>> courseGraph{};

        // Construct the graph
        for(auto prereq : prerequisites) {
            std::list<int> adjList{};
            // precheck for self cycles
            if(prereq[0] == prereq[1])
                return false;
            if(courseGraph.count(prereq[1]) != 0)
                courseGraph.at(prereq[1]).emplace_back(prereq[0]);
            else
             courseGraph.emplace(prereq[1], prereq[0]);
        }

        // Traverse the graph for cycles.
        std::unordered_set<int> isVisited{};
        std::queue<int> toVisit{};
        std::vector<bool> isChecked(numCourses, false);

        toVisit.emplace(courseGraph.begin()->first);

        for(int currNode = 0; currNode < numCourses; currNode++) {
            isChecked.at(currNode) = depthFirstSearch(courseGraph, currNode,
                                                      isChecked, std::unordered_set<int>{});
        }

        return true;
    }

private:
    bool depthFirstSearch(const std::unordered_map<int, std::list<int>>& courseGraph, int currCourse,
                            std::vector<bool> isChecked, std::unordered_set<int> isVisited) {
        std::list<int> adjList = courseGraph.at(currCourse);
        if(adjList.empty())
            return true;
        if(isVisited.count(currCourse) != 0)
            return false;
        if(isChecked.at(currCourse))
            return true;

        isVisited.emplace(currCourse);

        bool result = false;
        for(auto nextCourse : adjList){
            result = depthFirstSearch(courseGraph, nextCourse, isChecked, isVisited);
            if(not result)
                break;
        }

        isVisited.erase(currCourse);

        isChecked.at(currCourse);

        return result;
    }
};


#endif //LEETCODEGRIND_COURSESCHEDULE_H
