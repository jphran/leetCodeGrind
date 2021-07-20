//
// Created by jfrancis on 4/23/21.
//

#include <catch2/catch.hpp>
#include "graph/CourseSchedule.h"
#include <vector>


TEST_CASE("basic fn test for course schedule", "[CourseSchedule]") {
    int numCourses = 2;
    std::vector<std::vector<int>> prereqs = {{1, 0}};
    bool ans = true;

    Solution s;
    REQUIRE(s.canFinish(numCourses, prereqs) == ans);
}

TEST_CASE("basic fn test for course schedule1", "[CourseSchedule]") {
    int numCourses = 2;
    std::vector<std::vector<int>> prereqs = {{1, 0}, {0, 1}};
    bool ans = false;

    Solution s;
    REQUIRE(s.canFinish(numCourses, prereqs) == ans);
}

TEST_CASE("basic fn test for course schedule2", "[CourseSchedule]") {
    int numCourses = 20;
    std::vector<std::vector<int>> prereqs = {{0,10}, {3, 18}, {5, 5}, {6, 11}, {11, 14}, {13, 1}, {15, 1}, {17, 4}};
    bool ans = false;

    Solution s;
    REQUIRE(s.canFinish(numCourses, prereqs) == ans);
}
