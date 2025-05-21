"""
198. 打家劫舍

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一
制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。


示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。


提示：

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
import unittest


class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        dp数组
        @param nums:
        @return:
        """
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [0] * n
        for i in range(n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[n - 1]

    def rob1(self, nums: list[int]) -> int:
        """
        空间优化
        @param nums:
        @return:
        """
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        # rob1 存储到前两间房屋为止能偷窃到的最大金额 (dp[i-2])
        # rob2 存储到前一间房屋为止能偷窃到的最大金额 (dp[i-1])
        # 初始值都设为0，这样循环可以从头开始处理所有房屋
        rob1 = 0
        rob2 = 0
        for n in nums:
            # 对于当前房屋 num：
            # 1. 如果偷窃当前房屋，则金额为 num + rob1 (rob1 是跳过前一间房屋后，能获得的最大金额)
            # 2. 如果不偷窃当前房屋，则金额为 rob2 (rob2 是到前一间房屋为止能获得的最大金额)
            # current_rob_max 是两者中的较大值
            # current_rob_max = max(rob1 + n, rob2)
            # rob1 = rob2
            # rob2 = current_rob_max
            rob1, rob2 = rob2, max(rob1 + n, rob2)

        return rob2


class TestHouseRobber(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        nums = [1, 2, 3, 1]
        expected_money = 4 # (1 + 3)
        solution = Solution()
        actual_money = solution.rob(nums)
        self.assertEqual(actual_money, expected_money)
        actual_money = solution.rob1(nums)
        self.assertEqual(actual_money, expected_money)

    def test_example_2(self):
        # LeetCode 示例 2
        nums = [2, 7, 9, 3, 1]
        expected_money = 12 # (2 + 9 + 1)
        solution = Solution()
        actual_money = solution.rob(nums)
        self.assertEqual(actual_money, expected_money)
        actual_money = solution.rob1(nums)
        self.assertEqual(actual_money, expected_money)

    def test_single_house(self):
        # 只有一间房屋
        nums = [10]
        expected_money = 10
        solution = Solution()
        actual_money = solution.rob(nums)
        self.assertEqual(actual_money, expected_money)
        actual_money = solution.rob1(nums)
        self.assertEqual(actual_money, expected_money)

    def test_two_houses_first_greater(self):
        # 两间房屋，第一间金额更大
        nums = [2, 1]
        expected_money = 2
        solution = Solution()
        actual_money = solution.rob(nums)
        self.assertEqual(actual_money, expected_money)
        actual_money = solution.rob1(nums)
        self.assertEqual(actual_money, expected_money)

    def test_two_houses_second_greater(self):
        # 两间房屋，第二间金额更大
        nums = [1, 2]
        expected_money = 2
        solution = Solution()
        actual_money = solution.rob(nums)
        self.assertEqual(actual_money, expected_money)
        actual_money = solution.rob1(nums)
        self.assertEqual(actual_money, expected_money)

    def test_all_zeros(self):
        # 所有房屋金额都为 0
        nums = [0, 0, 0, 0]
        expected_money = 0
        solution = Solution()
        actual_money = solution.rob(nums)
        self.assertEqual(actual_money, expected_money)
        actual_money = solution.rob1(nums)
        self.assertEqual(actual_money, expected_money)

    def test_mixed_positive_negative_like_values(self):
        # 混合正负收益情景 (注意：题目约束 nums[i] >= 0，所以不会有负数金额)
        # 此测试用例仅为验证逻辑，实际不会出现负数金额
        # nums = [-2, 1, -3, 4] # Not applicable due to constraint 0 <= nums[i]
        pass # Skipping due to constraint clarification

    def test_long_array_with_complex_pattern(self):
        # 较长数组，复杂模式
        nums = [4, 1, 2, 7, 3, 1]
        expected_money = 12 # (4 + 7 + 1) -> 12. Trace:
        # rob1=0, rob2=0
        # num=4: temp=max(0+4,0)=4. rob1=0, rob2=4
        # num=1: temp=max(0+1,4)=4. rob1=4, rob2=4
        # num=2: temp=max(4+2,4)=6. rob1=4, rob2=6
        # num=7: temp=max(4+7,6)=11. rob1=6, rob2=11
        # num=3: temp=max(6+3,11)=11. rob1=11, rob2=11
        # num=1: temp=max(11+1,11)=12. rob1=11, rob2=12
        # Result: 12
        solution = Solution()
        actual_money = solution.rob(nums)
        self.assertEqual(actual_money, expected_money)
        actual_money = solution.rob1(nums)
        self.assertEqual(actual_money, expected_money)

    def test_another_complex_pattern(self):
        # 另一个复杂模式
        nums = [2, 1, 1, 2]
        expected_money = 4 # (2 + 2)
        solution = Solution()
        actual_money = solution.rob(nums)
        self.assertEqual(actual_money, expected_money)
        actual_money = solution.rob1(nums)
        self.assertEqual(actual_money, expected_money)

    def test_max_constraint_value(self):
        # 测试金额最大值
        nums = [400, 1, 400, 1, 400, 1]
        expected_money = 1200 # (400 + 400 + 400)
        solution = Solution()
        actual_money = solution.rob(nums)
        self.assertEqual(actual_money, expected_money)
        actual_money = solution.rob1(nums)
        self.assertEqual(actual_money, expected_money)


# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)