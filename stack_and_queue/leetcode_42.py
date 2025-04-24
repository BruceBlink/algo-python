"""
接雨水 (LeetCode 42)
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
示例 1：

  3  |_                    ___
  2  |_        ___        |  |___   ___
  1  |_  ___  |  |___   __|  |  |__|  |___
     |__|__|__|__|__|__|__|__|__|__|__|__|
      0  1  0  2  1  0  1  3  2  1  2  1
    输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出：6
    解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水。

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9
"""
import unittest


def trap1(heights: list[int]) -> int:
    """
    暴力解法
    """
    ans = 0
    n = len(heights)
    for i in range(n):
        # 计算height[i]左边的最大值
        max_left = 0
        for j in range(i):
            max_left = max(max_left, heights[j])
        max_right = 0
        for k in range(i + 1, n):
            max_right = max(max_right, heights[k])
        water = min(max_left, max_right) - heights[i]
        if water > 0:
            ans += water
    return ans


def trap2(heights: list[int]) -> int:
    """
    双指针
    """
    if not heights or len(heights) < 3:  # 至少需要三个柱子才能接水
        return 0
    left, right = 0, len(heights) - 1
    left_max = 0  # left指针左边的最高高度
    right_max = 0  # right指针右边的最高高度
    total_water = 0
    while left < right:
        if heights[left] < heights[right]:
            # 右边存在一个更高的柱子heights[right], 决定积水高度的是left_max
            if heights[left] > left_max:
                left_max = heights[left]  # 更新左边最高高度
            else:
                # 当前位置能接水，水量由left_max决定
                total_water += left_max - heights[left]
            left += 1  # 左指针右移动
        else:
            # 如果左边存在一个更高的（或者相等的）柱子heights[left], 决定积水高度取决右边的right_max
            if heights[right] > right_max:
                right_max = heights[right]  # 更新右边的最大高度
            else:
                # 当前位置能接水，水量由right_max决定
                total_water += right_max - heights[right]
            right -= 1  # 右指针左移
    return total_water


def trap3(heights: list[int]) -> int:
    """
    单调栈 解法
    """
    n = len(heights)
    # 处理输入数组为空或长度不足以形成凹槽的情况 (至少需要3个柱子)
    if not heights or n < 3:
        return 0

    res = 0  # 用于累计接到的雨水总量
    stack = []  # 用于存储柱子的索引。栈中存放的索引对应的柱子高度是单调递减的。

    # 遍历每一个柱子，i 是当前柱子的索引
    # 当前柱子 heights[i] 被视为可能的右边界
    for i in range(n):
        # 当栈不为空 并且 当前柱子 heights[i] 的高度 > 栈顶柱子 heights[stack[-1]] 的高度时：
        # 这意味着当前柱子比栈顶的柱子高，栈顶柱子找到了它右边第一个更高的柱子（当前柱子 i）。
        # 栈顶柱子 heights[stack[-1]] 此时成为了一个“谷底”或“中间的矮柱子”。
        while stack and heights[i] > heights[stack[-1]]:
            # 将栈顶的索引弹出。这个弹出的索引 mid_index 就对应了我们找到的“谷底”柱子。
            mid_index = stack.pop()
            # 在 while 循环的当前迭代中，刚刚弹出的 `mid_index` 对应的柱子 `heights[mid_index]`，
            # 确实是比当前柱子 `heights[i]` 要矮。而且由于栈的单调递减性质，`heights[mid_index]` 也比它下面那个
            # （现在成为了新的栈顶）柱子要矮。所以 `mid_index` 就是一个局部低点，是水槽的“底部”。

            # 检查弹出凹槽底后，栈是否为空。
            # 如果栈为空，说明这个凹槽左边没有更高的或相等的柱子来形成封闭的水槽了
            # （最左边的柱子无法形成水槽的左边界）。
            if not stack:
                break  # 跳出 while 循环，当前柱子 i 无法与之前的柱子形成有效水槽

            # 如果栈不为空，新的栈顶 stack[-1] 就是谷底柱子 mid_index 左边第一个比它高的柱子。
            # 它将作为水槽的左边界。
            left_index = stack[-1]

            # ===== 计算能接的雨水量 =====
            # 水槽的宽度 = 右边界索引 - 左边界索引 - 1 (减去谷底柱子本身的宽度)
            width = i - left_index - 1

            # 水槽的高度 = (左右边界柱子中较矮的那个) - 谷底柱子的高度
            # 雨水的高度是由左右两边的短板决定的。
            bounded_height = min(heights[left_index], heights[i]) - heights[mid_index]

            # 将这个水槽区域能接的雨水量累加到总结果中
            res += width * bounded_height

        # while 循环结束（栈为空，或者当前柱子高度小于等于栈顶柱子高度）：
        # 将当前柱子 i 的索引压入栈中。
        # 它现在成为了一个新的潜在的左边界，等待右边出现更高的柱子来形成水槽。
        # 由于 while 循环移除了所有小于等于 heights[i] 的栈顶元素，栈仍然保持单调递减。
        stack.append(i)

    # 遍历完所有柱子后，res 就是总的接雨水量
    return res


def trap4(heights: list[int]) -> int:
    # 处理输入数组为空的边缘情况。如果数组为空，无法接水。
    if not heights:
        return 0

    n = len(heights)  # 获取柱子的个数
    # 初始化用于存储每个位置左边最高高度的数组
    # left_max[i] 将存储从索引 0 到索引 i 的所有柱子中的最高高度
    left_max = [0] * n
    # 初始化用于存储每个位置左边最高高度的数组
    # left_max[i] 将存储从索引 0 到索引 i 的所有柱子中的最高高度
    right_max = [0] * n
    total_water = 0  # 初始化总的接雨水量为 0

    # ===== 第一步：计算 left_max 数组 =====
    # 从左向右遍历数组
    # left_max[0] 的左边没有其他柱子，所以它左边的最高高度就是它自身的高度
    left_max[0] = heights[0]
    # 从第二个柱子（索引 1）开始遍历到最后一个柱子（索引 n-1）
    for i in range(1, n):
        # 当前位置 i 的 left_max[i] 等于：
        # 当前柱子高度 height[i]
        # 和 前一个位置的 left_max[i-1] (即索引 0 到 i-1 的最高高度)
        # 两者中的较大值。
        # 这个是动态规划的状态转移方程：left_max[i] = max(height[i], left_max[i-1])
        left_max[i] = max(heights[i], left_max[i - 1])
    # ===== 第二步：计算 right_max 数组 =====
    # 从右向左遍历数组
    # right_max[n-1] 的右边没有其他柱子，所以它右边的最高高度就是它自身的高度
    right_max[n - 1] = heights[n - 1]
    # 从倒数第二个柱子（索引 n-2）开始遍历到第一个柱子（索引 0）
    # range(n - 2, -1, -1) 表示从 n-2 开始，到 -1 结束 (不包含 -1)，步长为 -1
    for i in range(n - 2, -1, -1):  # 反向遍历数组
        # 当前位置 i 的 right_max[i] 等于：
        # 当前柱子高度 height[i]
        # 和 后一个位置的 right_max[i+1] (即索引 i+1 到 n-1 的最高高度)
        # 两者中的较大值。
        # 状态转移方程：right_max[i] = max(height[i], right_max[i+1])
        right_max[i] = max(heights[i], right_max[i + 1])

    # ===== 第三步：计算总积水 =====
    # 再次遍历数组，对于每一个位置 i
    for i in range(n):
        # 计算在当前位置 i 上方理论上可以达到的水面高度。
        # 水面高度受限于左右两边最高的柱子中较矮的那个。
        water_level = min(left_max[i], right_max[i])

        # 计算当前位置 i 能够接住的雨水量。
        # 这是水面高度减去当前柱子的高度。
        trapped_at_i = water_level - heights[i]

        # 如果计算出的积水量大于 0 (水面高于柱子顶部)，说明这个位置确实能接住水。
        if trapped_at_i > 0:
            # 将这个位置的积水量累加到总雨水量中。
            total_water += trapped_at_i

    return total_water


class TestTrapSolution(unittest.TestCase):
    def setUp(self):
        self.height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    def test_trap1(self):
        self.assertEqual(trap1(self.height), 6)

    def test_trap2(self):
        self.assertEqual(trap2(self.height), 6)

    def test_trap3(self):
        self.assertEqual(trap1(self.height), 6)

    def test_trap4(self):
        self.assertEqual(trap1(self.height), 6)
