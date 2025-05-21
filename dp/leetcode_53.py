"""
53. 最大子数组和

给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），
返回其最大和。子数组是数组中的一个连续部分。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1
示例 3：
输入：nums = [5,4,-1,7,8]
输出：23

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""
import unittest


# The Solution class with the maxSubArray method (using Kadane's Algorithm)
# Solution 类，包含 maxSubArray 方法 (使用 Kadane's 算法)
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # 根据约束 1 <= nums.length，nums 保证非空，所以不需要显式检查空数组

        # max_so_far 存储全局最大子数组和
        # max_ending_here 存储以当前元素结尾的最大子数组和
        max_so_far = nums[0]
        max_ending_here = nums[0]

        # 从数组的第二个元素开始遍历
        for i in range(1, len(nums)):
            num = nums[i]

            # 决定是以当前元素开始一个新子数组，还是将当前元素加入到之前的子数组
            # 如果 max_ending_here (前一个子数组的和) 是负数，那么从 num 开始更好
            max_ending_here = max(num, max_ending_here + num)

            # 更新全局最大值
            max_so_far = max(max_so_far, max_ending_here)

        # 返回找到的最大子数组和
        return max_so_far


# Unit tests using unittest.TestCase
# 使用 unittest.TestCase 编写单元测试
class TestMaxSubArray(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected_sum = 6  # 子数组 [4,-1,2,1]
        solution = Solution()
        actual_sum = solution.maxSubArray(nums)
        self.assertEqual(actual_sum, expected_sum)

    def test_single_element_positive(self):
        # 单个元素，正数
        nums = [1]
        expected_sum = 1
        solution = Solution()
        actual_sum = solution.maxSubArray(nums)
        self.assertEqual(actual_sum, expected_sum)

    def test_single_element_negative(self):
        # 单个元素，负数 (必须包含至少一个元素)
        nums = [-1]
        expected_sum = -1
        solution = Solution()
        actual_sum = solution.maxSubArray(nums)
        self.assertEqual(actual_sum, expected_sum)

    def test_all_positive_elements(self):
        # 所有元素都是正数
        nums = [5, 4, -1, 7, 8]
        expected_sum = 23  # 整个数组
        solution = Solution()
        actual_sum = solution.maxSubArray(nums)
        self.assertEqual(actual_sum, expected_sum)

    def test_all_negative_elements(self):
        # 所有元素都是负数 (选择其中最大的一个)
        nums = [-2, -1, -3]
        expected_sum = -1  # 子数组 [-1]
        solution = Solution()
        actual_sum = solution.maxSubArray(nums)
        self.assertEqual(actual_sum, expected_sum)

    def test_mixed_elements_1(self):
        # 混合正负数
        nums = [1, 2, -1, 4, -5, 6]
        expected_sum = 7  # 子数组 [1,2,-1,4] 或 [4,-5,6]
        solution = Solution()
        actual_sum = solution.maxSubArray(nums)
        self.assertEqual(actual_sum, expected_sum)

    def test_mixed_elements_2(self):
        # 混合正负数，最大和在中间
        nums = [-1, 2, 3, -2, 4, -1]
        expected_sum = 7  # 子数组 [2,3,-2,4]
        solution = Solution()
        actual_sum = solution.maxSubArray(nums)
        self.assertEqual(actual_sum, expected_sum)

    def test_long_array_with_large_sum(self):
        # 较长的数组，较大的和
        nums = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
        expected_sum = 33  # 子数组 [12, 21] 33, from [10, -4, 3, 1, 5, 6] = 21, then [12, 21]
        # Let's trace this one:
        # current_max = 10, max_so_far = 10
        # num = -4: max( -4, 10-4=6) -> 6. max_so_far = max(10, 6) = 10
        # num = 3: max( 3, 6+3=9) -> 9. max_so_far = max(10, 9) = 10
        # num = 1: max( 1, 9+1=10) -> 10. max_so_far = max(10, 10) = 10
        # num = 5: max( 5, 10+5=15) -> 15. max_so_far = max(10, 15) = 15
        # num = 6: max( 6, 15+6=21) -> 21. max_so_far = max(15, 21) = 21
        # num = -35: max( -35, 21-35=-14) -> -14. max_so_far = max(21, -14) = 21
        # num = 12: max( 12, -14+12=-2) -> 12. max_so_far = max(21, 12) = 21
        # num = 21: max( 21, 12+21=33) -> 33. max_so_far = max(21, 33) = 33
        # num = -1: max( -1, 33-1=32) -> 32. max_so_far = max(33, 32) = 33
        # Correct.
        solution = Solution()
        actual_sum = solution.maxSubArray(nums)
        self.assertEqual(actual_sum, expected_sum)


# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
