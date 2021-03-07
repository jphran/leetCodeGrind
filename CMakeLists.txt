cmake_minimum_required(VERSION 3.17)
project(leetCodeGrind)

set(CMAKE_CXX_STANDARD 20)

include_directories(./include)

add_executable(${PROJECT_NAME} main.cpp
        include/LRUCache.h
        include/BestTimeToBuySellStock.h include/SumOfTwoIntegers.h include/NumberOf1Bits.h)

# TESTING
find_package(Catch2 REQUIRED)
add_executable(tests tests/testMain.cpp
        include/TwoSum.h src/TwoSum.cpp tests/testTwoSum.cpp
        include/LRUCache.h tests/testLRUCache.cpp
        include/CanPlaceFlowers.h tests/testCanPlaceFlowers.cpp
        include/BestTimeToBuySellStock.h tests/testBestTimeToBuySellStock.cpp include/SumOfTwoIntegers.h tests/testSumOfTwoIntegers.cpp include/NumberOf1Bits.h)
target_link_libraries(${PROJECT_NAME} Catch2::Catch2)
include(CTest)
include(ParseAndAddCatchTests)
ParseAndAddCatchTests(tests)