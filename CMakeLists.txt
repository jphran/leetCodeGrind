cmake_minimum_required(VERSION 3.17)
project(leetCodeGrind)

cmake_policy(SET CMP0110 NEW)
set(CMAKE_CXX_STANDARD 20)

include_directories(./include)

add_executable(${PROJECT_NAME} main.cpp
        include/LRUCache.h
        include/array/BestTimeToBuySellStock.h
        include/binary/SumOfTwoIntegers.h
        include/binary/NumberOf1Bits.h
        include/dynamic_programing/ClimbingStairs.h
        include/dynamic_programing/CoinChange.h
        include/linked_list/ReverseLinkedList.h
        include/matrix/SetMatrixZeroes.h
        include/string/LongestSubstringWithoutRepeatingCharacters.h
        include/tree/MaximumDepthOfBinaryTree.h
        include/array/ProductOfArrayExceptSelf.h
        include/binary/MissingNumber.h
        include/dynamic_programing/WordBreak.h
        include/FibSeq.h
        include/graph/CourseSchedule.h
        include/array/TwoSum2.h
        include/array/BestTimeToBuySellStock2.h
        include/array/ContainsDuplicate.h
        include/array/ProductOfArrayExceptSelf2.h
        include/array/ContainsDuplicate2.h
        include/array/MaximumSubarray.h
        include/array/MaxProfit_2021_12_16.h
        include/array/findMinInRotatedSortedArray.h include/array/SearchInRotatedSortedArray.h)

# TESTING
find_package(Catch2 REQUIRED)

add_executable(testTwoSum include/array/TwoSum.h tests/testTwoSum.cpp)
add_executable(testLRUCache include/LRUCache.h tests/testLRUCache.cpp)
add_executable(testCanPlaceFlowers include/CanPlaceFlowers.h tests/testCanPlaceFlowers.cpp)
add_executable(testBestTimeToBuySellStock include/array/BestTimeToBuySellStock.h tests/testBestTimeToBuySellStock.cpp include/array/BestTimeToBuySellStock2.h include/array/MaxProfit_2021_12_16.h)
add_executable(testSumOfTwoIntegers include/binary/SumOfTwoIntegers.h tests/testSumOfTwoIntegers.cpp)
add_executable(testClimbingStairs include/dynamic_programing/ClimbingStairs.h tests/testClimbingStairs.cpp)
add_executable(testCoinChange include/dynamic_programing/CoinChange.h tests/testCoinChange.cpp)
add_executable(testReverseLinkedList tests/testReverseLinkedList.cpp)
add_executable(testSetMatrixZeroes include/matrix/SetMatrixZeroes.h tests/testSetMatrixZeroes.cpp)
add_executable(testLongestSubstringWithoutRepeatingCharacters include/string/LongestSubstringWithoutRepeatingCharacters.h tests/testLongestSubstringWithoutRepeatingCharacters.cpp)
add_executable(testMaximumDepthOfBinaryTree include/tree/MaximumDepthOfBinaryTree.h tests/testMaximumDepthOfBinaryTree.cpp)
add_executable(testProductOfArrayExceptSelf include/array/ProductOfArrayExceptSelf.h tests/testProductOfArrayExceptSelf.cpp include/array/ProductOfArrayExceptSelf2.h)
add_executable(testFibSeq include/FibSeq.h tests/testWordBreak.cpp include/graph/CourseSchedule.h tests/testCourseSchedule.cpp)
add_executable(testContainsDuplicate include/array/ContainsDuplicate.h tests/testContainsDuplicate.cpp include/array/ContainsDuplicate2.h)
add_executable(testMaximumSubarray include/array/MaximumSubarray.h tests/testMaximumSubarray.cpp)
add_executable(testMaximumProductSubarray include/array/MaximumProductSubarray.h tests/testMaximumProductSubarray.cpp)
add_executable(testFindMinInSortedArray include/array/findMinInRotatedSortedArray.h tests/testFindMinInSortedArray.cpp)
add_executable(testSearchInRotatedSortedArray tests/testSearchInRotatedSortedArray.cpp include/array/SearchInRotatedSortedArray.h)

target_link_libraries(${PROJECT_NAME} Catch2::Catch2)
