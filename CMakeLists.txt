cmake_minimum_required(VERSION 3.17)
project(leetCodeGrind)

set(CMAKE_CXX_STANDARD 20)

include_directories(./include)

add_executable(${PROJECT_NAME} main.cpp
        include/TwoSum.h src/TwoSum.cpp
        include/LRUCache.h include/CanPlaceFlowers.h)

# TESTING
find_package(Catch2 REQUIRED)
add_executable(tests tests/testMain.cpp
        include/TwoSum.h src/TwoSum.cpp
        include/LRUCache.h
        tests/testTwoSum.cpp
        tests/testLRUCache.cpp include/CanPlaceFlowers.h tests/testCanPlaceFlowers.h.cpp)
target_link_libraries(${PROJECT_NAME} Catch2::Catch2)
include(CTest)
include(ParseAndAddCatchTests)
ParseAndAddCatchTests(tests)