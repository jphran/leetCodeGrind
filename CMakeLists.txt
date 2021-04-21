cmake_minimum_required(VERSION 3.17)
project(leetCodeGrind)

set(CMAKE_CXX_STANDARD 20)

include_directories(./include)

add_executable(${PROJECT_NAME} main.cpp
        include/LRUCache.h
        include/BestTimeToBuySellStock.h
        include/SumOfTwoIntegers.h
        include/NumberOf1Bits.h
        include/ClimbingStairs.h
        include/CoinChange.h
        include/ReverseLinkedList.h
        include/SetMatrixZeroes.h
        include/string/LongestSubstringWithoutRepeatingCharacters.h include/tree/MaximumDepthOfBinaryTree.h)

# TESTING
find_package(Catch2 REQUIRED)
add_executable(tests tests/testMain.cpp
        include/TwoSum.h tests/testTwoSum.cpp
        include/LRUCache.h tests/testLRUCache.cpp
        include/CanPlaceFlowers.h tests/testCanPlaceFlowers.cpp
        include/BestTimeToBuySellStock.h tests/testBestTimeToBuySellStock.cpp
        include/SumOfTwoIntegers.h tests/testSumOfTwoIntegers.cpp
        include/NumberOf1Bits.h
        include/ClimbingStairs.h tests/testClimbingStairs.cpp
        include/CoinChange.h tests/testCoinChange.cpp
        tests/testReverseLinkedList.cpp
        include/SetMatrixZeroes.h tests/testSetMatrixZeroes.cpp
        include/string/LongestSubstringWithoutRepeatingCharacters.h tests/testLongestSubstringWithoutRepeatingCharacters.cpp include/tree/MaximumDepthOfBinaryTree.h tests/testMaximumDepthOfBinaryTree.cpp)
target_link_libraries(${PROJECT_NAME} Catch2::Catch2)
include(CTest)
include(ParseAndAddCatchTests)
ParseAndAddCatchTests(tests)