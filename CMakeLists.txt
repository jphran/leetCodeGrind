cmake_minimum_required(VERSION 3.17)
project(leetCodeGrind)

cmake_policy(SET CMP0110 NEW)
set(CMAKE_CXX_STANDARD 20)

include_directories(./include)

add_executable(${PROJECT_NAME} main.cpp
        include/LRUCache.h
        include/array/PostSarcos/BestTimeToBuySellStock.h
        include/binary/PostSarcos/SumOfTwoIntegers.h
        include/binary/PostSarcos/NumberOf1Bits.h
        include/dynamic_programing/PostSarcos/ClimbingStairs.h
        include/dynamic_programing/PostSarcos/CoinChange.h
        include/linked_list/ReverseLinkedList.h
        include/matrix/SetMatrixZeroes.h
        include/string/LongestSubstringWithoutRepeatingCharacters.h
        include/tree/MaximumDepthOfBinaryTree.h
        include/array/PostSarcos/ProductOfArrayExceptSelf.h
        include/binary/PostSarcos/MissingNumber.h
        include/dynamic_programing/PostSarcos/WordBreak.h
        include/FibSeq.h
        include/graph/CourseSchedule.h
        include/array/PostNimble/TwoSum2.h
        include/array/PostNimble/BestTimeToBuySellStock2.h
        include/array/PostSarcos/ContainsDuplicate.h
        include/array/PostNimble/ProductOfArrayExceptSelf2.h
        include/array/PostNimble/ContainsDuplicate2.h
        include/array/PostNimble/MaximumSubarray.h
        include/array/PostSarcos/MaxProfit_2021_12_16.h
        include/array/PostSarcos/findMinInRotatedSortedArray.h include/array/PostNimble/SearchInRotatedSortedArray.h include/array/PostNimble/ThreeSum.h include/array/PostNimble/MaxArea.h include/binary/PostNimble/SumOfTwoIntegers.h include/binary/PostNimble/NumberOfOneBits.h include/binary/PostNimble/CountingBits.h include/binary/PostNimble/MissingNumber.h include/binary/PostNimble/ReverseBits.h include/dynamic_programing/PostNimble/ClimbingStairs.h include/dynamic_programing/PostNimble/CoinChange.h include/dynamic_programing/PostNimble/LongestIncreasingSubsequence.h include/dynamic_programing/PostNimble/LongestCommonSubsequence.h include/dynamic_programing/PostNimble/WordBreak.h include/dynamic_programing/PostNimble/CombinatinSumIV.h)

# TESTING
find_package(Catch2 REQUIRED)

add_executable(testTwoSum include/array/PostSarcos/TwoSum.h tests/testTwoSum.cpp)
add_executable(testLRUCache include/LRUCache.h tests/testLRUCache.cpp)
add_executable(testCanPlaceFlowers include/CanPlaceFlowers.h tests/testCanPlaceFlowers.cpp)
add_executable(testBestTimeToBuySellStock include/array/PostSarcos/BestTimeToBuySellStock.h tests/testBestTimeToBuySellStock.cpp include/array/PostNimble/BestTimeToBuySellStock2.h include/array/PostSarcos/MaxProfit_2021_12_16.h)
add_executable(testSumOfTwoIntegers include/binary/PostSarcos/SumOfTwoIntegers.h include/binary/PostNimble/SumOfTwoIntegers.h tests/binary/testSumOfTwoIntegers.cpp)
add_executable(testClimbingStairs include/dynamic_programing/PostSarcos/ClimbingStairs.h include/dynamic_programing/PostNimble/ClimbingStairs.h tests/testClimbingStairs.cpp)
add_executable(testCoinChange include/dynamic_programing/PostSarcos/CoinChange.h tests/testCoinChange.cpp include/dynamic_programing/PostNimble/CoinChange.h)
add_executable(testReverseLinkedList tests/testReverseLinkedList.cpp)
add_executable(testSetMatrixZeroes include/matrix/SetMatrixZeroes.h tests/testSetMatrixZeroes.cpp)
add_executable(testLongestSubstringWithoutRepeatingCharacters include/string/LongestSubstringWithoutRepeatingCharacters.h tests/testLongestSubstringWithoutRepeatingCharacters.cpp)
add_executable(testMaximumDepthOfBinaryTree include/tree/MaximumDepthOfBinaryTree.h tests/testMaximumDepthOfBinaryTree.cpp)
add_executable(testProductOfArrayExceptSelf include/array/PostSarcos/ProductOfArrayExceptSelf.h tests/testProductOfArrayExceptSelf.cpp include/array/PostNimble/ProductOfArrayExceptSelf2.h)
add_executable(testFibSeq include/FibSeq.h tests/testWordBreak.cpp include/graph/CourseSchedule.h tests/testCourseSchedule.cpp)
add_executable(testContainsDuplicate include/array/PostSarcos/ContainsDuplicate.h tests/testContainsDuplicate.cpp include/array/PostNimble/ContainsDuplicate2.h)
add_executable(testMaximumSubarray include/array/PostNimble/MaximumSubarray.h tests/testMaximumSubarray.cpp)
add_executable(testMaximumProductSubarray include/array/PostNimble/MaximumProductSubarray.h tests/testMaximumProductSubarray.cpp)
add_executable(testFindMinInSortedArray include/array/PostSarcos/findMinInRotatedSortedArray.h tests/testFindMinInSortedArray.cpp)
add_executable(testSearchInRotatedSortedArray tests/testSearchInRotatedSortedArray.cpp include/array/PostNimble/SearchInRotatedSortedArray.h)
add_executable(testThreeSum tests/testThreeSum.cpp include/array/PostNimble/ThreeSum.h)
add_executable(testContainerWithMostWater tests/testMaxArea.cpp include/array/PostNimble/MaxArea.h)

target_link_libraries(${PROJECT_NAME} Catch2::Catch2)
