"""
322. 零钱兑换

给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。


示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0


提示：

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""
import functools
import unittest


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        def dp(_coins, _amount) -> int:
            if _amount == 0:
                return 0
            if _amount < 0:
                return -1
            res = float("inf")
            for coin in _coins:
                # 计算子问题
                sub_problem = dp(_coins, _amount - coin)
                if sub_problem == -1:
                    continue
                res = min(res, sub_problem + 1)
            if res == float("inf"):
                return -1
            else:
                return res

        return dp(coins, amount)

    def coinChange1(self, coins: list[int], amount: int) -> int:
        # memo 用于存储已经计算过的子问题的结果
        # key: 子问题的目标金额 (_amount)
        # value: 凑成该金额所需的最少硬币数
        memo = {}

        # 内部递归函数，进行记忆化搜索
        # 将 _coins 参数移除，因为 coins 列表在整个过程中是固定的，可以直接访问外层变量
        def dp(_amount: int) -> int:
            # 1. 记忆化：如果当前子问题已经计算过，直接返回结果
            if _amount in memo:
                return memo[_amount]

            # 2. 基本情况
            if _amount == 0:
                return 0
            if _amount < 0:  # 目标金额为负数，表示此路径无效
                return -1

            # 3. 递归计算 (状态转移)
            # 初始化结果为无穷大，表示目前还没有找到有效的方法
            res = float("inf")

            # 遍历所有硬币面额
            for coin in coins:  # 直接使用外层作用域的 'coins'
                # 递归计算子问题：凑成 _amount - coin 所需的最少硬币数
                sub_problem_res = dp(_amount - coin)

                # 如果子问题无法凑成 (返回 -1)，则当前硬币无法引导到有效解，跳过
                if sub_problem_res == -1:
                    continue

                # 更新 res：取当前 res 和 (子问题结果 + 1) 的最小值
                # +1 是因为我们使用了当前这枚 coin
                res = min(res, sub_problem_res + 1)

            # 4. 存储结果并返回
            # 如果 res 仍然是无穷大，表示无论尝试了所有硬币，都无法凑成 _amount
            if res == float("inf"):
                memo[_amount] = -1  # 标记为 -1 (不可达)
                return -1
            else:
                memo[_amount] = res  # 存储计算出的最少硬币数
                return res

        # 从主函数调用递归入口，开始计算目标 amount
        return dp(amount)

    def coinChange2(self, coins: list[int], amount: int) -> int:
        # 使用 @functools.lru_cache(None) 来为 dp 函数添加记忆化功能。
        # None 表示缓存大小无限制，所有计算过的结果都会被存储。
        @functools.lru_cache(None)
        def dp(_amount: int) -> int:
            # 基本情况 (Base Cases)
            if _amount == 0:
                return 0  # 凑成金额 0 需要 0 个硬币
            if _amount < 0:
                return -1  # 金额为负数，表示此路径无效

            # 初始化结果为无穷大，表示目前还没有找到凑成当前金额的方法
            res = float("inf")

            # 遍历所有硬币面额
            # 直接使用外层函数作用域的 'coins' 变量，无需作为参数传入
            for coin in coins:
                # 递归计算子问题：凑成 _amount - coin 所需的最少硬币数
                sub_problem_res = dp(_amount - coin)

                # 如果子问题无法凑成 (返回 -1)，则跳过当前硬币，尝试下一个
                if sub_problem_res == -1:
                    continue

                # 更新 res：取当前 res 和 (子问题结果 + 1) 的最小值
                # +1 是因为我们使用了当前这枚 coin
                res = min(res, sub_problem_res + 1)

            # 返回最终结果：
            # 如果 res 仍然是无穷大，表示无法凑成当前金额，返回 -1
            # 否则，返回计算出的最少硬币数
            return res if res != float("inf") else -1

        # 从主函数调用记忆化后的递归函数入口，开始计算目标 amount
        return dp(amount)

    def coinChange3(self, coins: list[int], amount: int) -> int:
        # 创建一个 dp 数组，dp[i] 存储凑成金额 i 所需的最少硬币数。
        # 数组大小为 amount + 1，索引从 0 到 amount。
        # 初始化所有值为 amount + 1，这比任何可能的有效结果都大，
        # 充当“无限大”的值，表示该金额目前不可达。
        dp = [amount + 1] * (amount + 1)

        # 基本情况：凑成金额 0 需要 0 个硬币
        dp[0] = 0

        # 外层循环：遍历所有可能的金额，从 1 到 amount
        for i in range(1, amount + 1):
            # 内层循环：遍历每种硬币面额
            for coin in coins:
                # 如果当前金额 i 大于或等于当前硬币面额 coin
                if i >= coin:
                    # 状态转移方程：
                    # dp[i] = min(当前的 dp[i]值, 1 + dp[i - coin]的值)
                    # 1 + dp[i - coin] 表示：使用一个当前硬币 coin，
                    # 然后再凑齐剩下的 i - coin 金额所需的最少硬币数。
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        # 最终结果：
        # 如果 dp[amount] 仍然是初始的“无限大”值 (amount + 1)，
        # 说明目标金额无法凑成，返回 -1。
        # 否则，返回计算出的最少硬币数。
        return dp[amount] if dp[amount] != amount + 1 else -1


class TestCoinChange(unittest.TestCase):

    def test_example_1(self):
        # LeetCode 示例 1
        coins = [1, 2, 5]
        amount = 11
        expected_sum = 3  # 解释：11 = 5 + 5 + 1
        solution = Solution()
        actual_sum = solution.coinChange(coins, amount)
        self.assertEqual(actual_sum, expected_sum)
