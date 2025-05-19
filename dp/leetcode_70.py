"""
70. 爬楼梯

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

示例 2：
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶

提示：

1 <= n <= 45

"""
import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        # 处理基本情况
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev_1 = 1  # 存储爬到第 i-2 阶的方法数 (初始为爬到第 1 阶的方法数)
        prev_2 = 2  # 存储爬到第 i-1 阶的方法数 (初始为爬到第 2 阶的方法数)
        # 从第 3 阶开始计算，直到第 n 阶
        for i in range(3, n + 1):
            # 当前阶爬楼梯的方法数 = 前一阶方法数 + 前两阶的方法数
            current_ways = prev_1 + prev_2
            # 更新prev_1 和 prev_2位下一轮做准备
            prev_1, prev_2 = prev_2, current_ways
        return prev_2

    def climbStairs_dp_array(self, n: int) -> int:
        # 处理基本情况
        if n == 1:
            return 1
        if n == 2:
            return 2

        # 创建 DP 数组
        dp = [0] * (n + 1)

        # 初始化基本情况
        dp[1] = 1
        dp[2] = 2

        # 填充 DP 数组
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # 返回结果
        return dp[n]


class TestClimbStairs(unittest.TestCase):

    def test_n_is_1(self):
        # 爬 1 阶
        n = 1
        expected_ways = 1
        solution = Solution()
        actual_ways = solution.climbStairs(n)
        self.assertEqual(actual_ways, expected_ways)

    def test_n_is_2(self):
        # 爬 2 阶
        n = 2
        expected_ways = 2
        solution = Solution()
        actual_ways = solution.climbStairs(n)
        self.assertEqual(actual_ways, expected_ways)

    def test_n_is_3(self):
        # 爬 3 阶
        n = 3
        expected_ways = 3  # (1+1+1), (1+2), (2+1)
        solution = Solution()
        actual_ways = solution.climbStairs(n)
        self.assertEqual(actual_ways, expected_ways)

    def test_n_is_4(self):
        # 爬 4 阶
        n = 4
        expected_ways = 5  # (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2)
        solution = Solution()
        actual_ways = solution.climbStairs(n)
        self.assertEqual(actual_ways, expected_ways)

    def test_n_is_5(self):
        # 爬 5 阶
        n = 5
        expected_ways = 8
        solution = Solution()
        actual_ways = solution.climbStairs(n)
        self.assertEqual(actual_ways, expected_ways)

    def test_n_is_10(self):
        # 爬 10 阶 (斐波那契序列)
        n = 10
        expected_ways = 89
        solution = Solution()
        actual_ways = solution.climbStairs(n)
        self.assertEqual(actual_ways, expected_ways)

    def test_n_is_45(self):
        # 爬 45 阶 (接近约束上限)
        n = 45
        # 45th Fibonacci number starting 1, 2, 3...
        expected_ways = 1836311903
        solution = Solution()
        actual_ways = solution.climbStairs(n)
        self.assertEqual(actual_ways, expected_ways)


# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
