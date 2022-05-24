"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        product_except_self = [1 for _ in range(n)]

        product_from_right = 1
        for i in range(n):
            product_except_self[i] = product_from_right
            product_from_right *= nums[i]

        product_from_left = 1
        for i in reversed(range(n)):
            product_except_self[i] *= product_from_left
            product_from_left *= nums[i]

        return product_except_self


        # INIT ATTEMPT, works, just slow
        # left_product: list[int] = [1] * len(nums)
        # right_product: list[int] = [1] * len(nums)
        #
        # for i in range(1, len(nums)):
        #     left_product[i] = nums[i - 1] * left_product[i - 1]
        #     right_product[-i - 1] = nums[-i] * right_product[-i]
        #
        # for i in range(len(nums)):
        #     nums[i] = left_product[i] * right_product[i]
        #
        # return nums

