"""
给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。

由于答案可能很大，因此 返回答案模 10^9 + 7 。



示例 1：

输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
示例 2：

输入：arr = [11,81,94,43,3]
输出：444


提示：

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
"""
import unittest


def sum_sub_array_mins_brute_force(arr: list[int]) -> int:
    mod = 10 ** 9 + 7  # 定义模数
    n = len(arr)
    total_sum = 0  # 初始化总和

    # 外层循环：遍历所有可能的子数组的起始位置 l
    for l in range(n):
        # 内层循环：遍历所有可能的子数组的结束位置 r (r >= l)
        # 对于固定的 l，随着 r 的增加，我们构建并考虑子数组 arr[l...r]
        current_min = float('inf')  # 用于记录当前子数组 arr[l...r] 的最小值

        for r in range(l, n):
            # 在内层循环中，随着 r 的增加，当前子数组 arr[l...r] 包含 arr[r]
            # 我们可以 O(1) 地更新当前子数组的最小值
            current_min = min(current_min, arr[r])

            # 将当前子数组 arr[l...r] 的最小值加到总和中
            total_sum = (total_sum + current_min) % mod

    return total_sum


def sum_sub_array_mins(arr: list[int]) -> int:
    mod = 10 ** 9 + 7
    n = len(arr)

    # left_smaller[i] 存储 arr[i] 左边第一个严格小于 arr[i] 的元素的索引
    # 如果不存在，则为 -1
    left_smaller = [-1] * n

    # right_smaller_equal[i] 存储 arr[i] 右边第一个小于等于 arr[i] 的元素的索引
    # 如果不存在，则为 n
    right_smaller_equal = [n] * n

    stack = []  # 单调递增栈，存储索引

    # ===== 计算 left_smaller 数组 =====
    # 从左往右遍历
    for i in range(n):
        # 保持栈的单调递增：如果栈不为空且当前元素小于等于栈顶元素，弹出栈顶
        # （这里我们找左边第一个严格小于，所以遇到等于也要弹出，等右边处理）
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()

        # 如果栈不为空，栈顶元素就是左边第一个严格小于 arr[i] 的元素索引
        if stack:
            left_smaller[i] = stack[-1]

        # 将当前索引压入栈
        stack.append(i)

    # 清空栈，用于计算 right_smaller_equal
    stack = []

    # ===== 计算 right_smaller_equal 数组 =====
    # 从右往左遍历
    for i in range(n - 1, -1, -1):
        # 保持栈的单调递增：如果栈不为空且当前元素严格小于栈顶元素，弹出栈顶
        # （这里我们找右边第一个小于等于，遇到等于不弹出，保证左边严格小于的元素优先配对）
        while stack and arr[i] < arr[stack[-1]]:
            stack.pop()

        # 如果栈不为空，栈顶元素就是右边第一个小于等于 arr[i] 的元素索引
        if stack:
            right_smaller_equal[i] = stack[-1]

        # 将当前索引压入栈
        stack.append(i)

    # ===== 计算总和 =====
    total_sum = 0
    for i in range(n):
        # 计算左边界和右边界的距离
        # 左边边界数量：i - left_smaller[i] (从 left_smaller[i] + 1 到 i)
        # 右边边界数量：right_smaller_equal[i] - i (从 i 到 right_smaller_equal[i] - 1)
        left_count = i - left_smaller[i]
        right_count = right_smaller_equal[i] - i

        # arr[i] 作为最小值的子数组数量 = left_count * right_count
        # arr[i] 对总和的贡献 = arr[i] * 数量
        contribution = (arr[i] * left_count * right_count) % mod

        total_sum = (total_sum + contribution) % mod

    return total_sum


class TestSumSubArrayMins(unittest.TestCase):

    def test_sum_sub_array_mins_brute_force(self):
        self.assertEqual(sum_sub_array_mins_brute_force([3, 1, 2, 4]), 17)
        self.assertEqual(sum_sub_array_mins_brute_force([11, 81, 94, 43, 3]), 444)

    def test_sum_sub_array_mins(self):
        self.assertEqual(sum_sub_array_mins([3, 1, 2, 4]), 17)
        self.assertEqual(sum_sub_array_mins([11, 81, 94, 43, 3]), 444)
