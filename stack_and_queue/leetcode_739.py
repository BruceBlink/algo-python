import unittest


class DailyTemperature:
    """
    每日温度（LeetCode 739）
    给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
    示例 1:
    输入: temperatures = [73,74,75,71,69,72,76,73]
    输出: [1,1,4,2,1,1,0,0]

    示例 2:
    输入: temperatures = [30,40,50,60]
    输出: [1,1,1,0]

    示例 3:
    输入: temperatures = [30,60,90]
    输出: [1,1,0]

    提示：
    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100

    :param self:
    :param temp: 温度列表
    :return: 结果列表
    """

    @staticmethod
    def daily_temperatures(temperature: list[int]) -> list[int]:
        """
        暴力解法
        """
        n = len(temperature)
        answer = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if temperature[j] > temperature[i]:
                    answer[i] = j - i
                    break
        return answer

    @staticmethod
    def daily_temperatures1(temperature: list[int]) -> list[int]:
        """
        单调栈解法
        """
        n = len(temperature)
        answer = [0] * n  # 初始化结果列表
        stack = []  # 初始化栈，存储待处理的索引

        # 从左往右遍历每一天的温度，i 是当前天的索引
        for i in range(n):
            # 当栈不为空 并且 当前温度 temperature[i] 大于 栈顶索引对应的温度 temperature[stack[-1]] 时
            while stack and temperature[i] > temperature[stack[-1]]:
                # 弹出栈顶的索引 top_index
                top_index = stack.pop()

                # 计算等待的天数 (i - top_index)，并将其记录在 answer[top_index] 位置
                answer[top_index] = i - top_index

            # 将当前天的索引 i 压入栈中，等待未来出现比它更高的温度
            stack.append(i)

        # 遍历完所有温度后，answer 列表就是最终结果
        return answer


class TestDailyTemperature(unittest.TestCase):

    def setUp(self):
        self.temps = [73, 74, 75, 71, 69, 72, 76, 73]
        self.dt = DailyTemperature()

    def test_daily_temperatures(self):
        self.assertEqual(DailyTemperature.daily_temperatures(self.temps), [1, 1, 4, 2, 1, 1, 0, 0])

    def test_daily_temperatures1(self):
        self.assertEqual(DailyTemperature.daily_temperatures1(self.temps), [1, 1, 4, 2, 1, 1, 0, 0])
