"""
121. 买卖股票的最佳时机
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。
设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

提示：

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4

"""
import unittest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 根据约束 1 <= prices.length，数组至少包含一个元素，无需检查空数组。
        # 如果数组只有一个元素，循环不会执行，max_profit 仍为 0，符合要求。

        # min_price 记录到当前为止的最低买入价格
        # 初始化为无穷大，确保任何价格都会被更新为新的最低价
        min_price = float('inf')

        # max_profit 记录到当前为止的最大利润
        # 初始化为 0，因为如果没有利润，题目要求返回 0
        max_profit = 0

        # 遍历每一天的股票价格
        for price in prices:
            # 更新最低买入价格：
            # 如果当前价格比 min_price 更低，就把它作为新的最低买入点
            min_price = min(min_price, price)

            # 计算当前价格卖出能获得的利润：
            # 利润 = 当前价格 - 历史最低买入价
            # 然后更新最大利润，取当前计算的利润和 max_profit 中的较大值
            max_profit = max(max_profit, price - min_price)

        # 返回最终的最大利润
        return max_profit


# Unit tests using unittest.TestCase
# 使用 unittest.TestCase 编写单元测试
class TestMaxProfit(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        prices = [7, 1, 5, 3, 6, 4]
        expected_profit = 5  # 买入价 1 (第2天), 卖出价 6 (第5天)
        solution = Solution()
        actual_profit = solution.maxProfit(prices)
        self.assertEqual(actual_profit, expected_profit)

    def test_example_2_decreasing_prices(self):
        # LeetCode 示例 2: 价格递减，无利润
        prices = [7, 6, 4, 3, 1]
        expected_profit = 0
        solution = Solution()
        actual_profit = solution.maxProfit(prices)
        self.assertEqual(actual_profit, expected_profit)

    def test_ascending_prices(self):
        # 价格递增，最大利润在最后一天卖出
        prices = [1, 2, 3, 4, 5]
        expected_profit = 4  # 买入价 1 (第1天), 卖出价 5 (第5天)
        solution = Solution()
        actual_profit = solution.maxProfit(prices)
        self.assertEqual(actual_profit, expected_profit)

    def test_small_case_buy_second_sell_last(self):
        # 较小数组，买入在中间
        prices = [2, 1, 4]
        expected_profit = 3  # 买入价 1 (第2天), 卖出价 4 (第3天)
        solution = Solution()
        actual_profit = solution.maxProfit(prices)
        self.assertEqual(actual_profit, expected_profit)

    def test_two_days_profit(self):
        # 只有两天，有利润
        prices = [1, 2]
        expected_profit = 1
        solution = Solution()
        actual_profit = solution.maxProfit(prices)
        self.assertEqual(actual_profit, expected_profit)

    def test_single_day(self):
        # 只有一天，无利润 (根据题目约束，不能同一天买卖)
        prices = [10]
        expected_profit = 0
        solution = Solution()
        actual_profit = solution.maxProfit(prices)
        self.assertEqual(actual_profit, expected_profit)

    def test_flat_prices(self):
        # 价格保持不变
        prices = [5, 5, 5, 5]
        expected_profit = 0
        solution = Solution()
        actual_profit = solution.maxProfit(prices)
        self.assertEqual(actual_profit, expected_profit)

    def test_complex_pattern(self):
        # 复杂的价格波动
        prices = [3, 3, 5, 0, 0, 3, 1, 4]
        expected_profit = 4  # 买入价 0 (第4天/第5天), 卖出价 4 (第8天)
        solution = Solution()
        actual_profit = solution.maxProfit(prices)
        self.assertEqual(actual_profit, expected_profit)

    def test_zero_prices(self):
        # 价格为 0
        prices = [0, 0, 0, 0, 0]
        expected_profit = 0
        solution = Solution()
        actual_profit = solution.maxProfit(prices)
        self.assertEqual(actual_profit, expected_profit)


# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
