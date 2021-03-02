cmake_minimum_required(VERSION 3.17)
project(leetCodeGrind)

set(CMAKE_CXX_STANDARD 20)

include_directories(./include)

add_executable(${PROJECT_NAME} main.cpp
        include/TwoSum.h src/TwoSum.cpp
        include/LRUCache.h)

find_package(Catch2 REQUIRED)
add_executable(tests tests/test.cpp
        include/TwoSum.h src/TwoSum.cpp
        include/LRUCache.h)
target_link_libraries(${PROJECT_NAME} Catch2::Catch2)
include(CTest)
include(ParseAndAddCatchTests)
ParseAndAddCatchTests(tests)