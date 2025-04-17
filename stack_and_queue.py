from typing import List, Any


class MinStack:
    """
    最小栈（LeetCode 155）
    描述：设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, num: int):
        self.stack.append(num)
        # 如果 min_stack为空或者stack的栈顶元素小于min_stack的栈顶元素
        if not self.min_stack or self.stack[-1] <= self.min_stack[-1]:
            self.min_stack.append(num)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]


import unittest


class TestMinStack(unittest.TestCase):

    def setUp(self):
        self.min_stack = MinStack()
        self.min_stack.push(1)
        self.min_stack.push(2)
        self.min_stack.push(3)
        self.min_stack.push(4)
        self.min_stack.push(5)

    def test_get_min(self):
        self.assertEqual(self.min_stack.get_min(), 1)
        self.min_stack.push(0)
        self.assertEqual(self.min_stack.get_min(), 0)

    def test_top(self):
        self.assertEqual(self.min_stack.top(), 5)
        self.min_stack.push(0)
        self.assertEqual(self.min_stack.top(), 0)

    def test_pop(self):
        self.assertEqual(self.min_stack.top(), 5)
        self.min_stack.pop()
        self.assertEqual(self.min_stack.top(), 4)


class MyQueue:
    """
    用栈实现队列（LeetCode 225）
    描述：请你仅使用两个栈实现一个先入先出（FIFO）的队列，并支持普通队列的全部操作（push，pop，peek，empty）。
    """

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, val: int) -> None:
        """
        入队列
        """
        self.in_stack.append(val)

    def pop(self) -> int:
        """
        出队列并返回队首元素
        :return:队首元素
        """
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int | None:
        """
        查看队首元素
        :return: 队首元素
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            return self.out_stack[-1]

    def empty(self) -> bool:
        """
        判断队列时候为空
        :return:
        """
        return not self.in_stack and not self.out_stack


class TestMyQueue(unittest.TestCase):

    def setUp(self):
        self.my_queue = MyQueue()
        self.my_queue.push(1)
        self.my_queue.push(2)
        self.my_queue.push(3)
        self.my_queue.push(4)
        self.my_queue.push(5)

    def test_push(self):
        self.my_queue.push(1)
        self.assertEqual(self.my_queue.peek(), 1)

    def test_pop(self):
        self.assertEqual(self.my_queue.pop(), 1)
        self.assertEqual(self.my_queue.pop(), 2)
        self.assertEqual(self.my_queue.pop(), 3)
        self.assertEqual(self.my_queue.pop(), 4)
        self.assertEqual(self.my_queue.pop(), 5)

    def test_peek(self):
        self.assertEqual(self.my_queue.peek(), 1)

    def test_empty(self):
        self.assertFalse(self.my_queue.empty())
        self.my_queue = MyQueue()
        self.assertTrue(self.my_queue.empty())


from collections import deque


class MyStack:
    """
    用队列实现栈（LeetCode 232）
    描述：请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部操作（push，top，pop，empty）。
    """

    def __init__(self):
        self.dq = deque()

    def push(self, val: int) -> None:
        self.dq.append(val)
        for _ in range(len(self.dq) - 1):
            self.dq.append(self.dq.popleft())

    def top(self) -> int:
        return self.dq[0]

    def pop(self) -> int:
        return self.dq.popleft()

    def empty(self) -> bool:
        return not self.dq


class TestMyStack(unittest.TestCase):
    def setUp(self):
        self.my_stack = MyStack()
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.my_stack.push(3)

    def test_push_and_top(self):
        self.assertEqual(len(self.my_stack.dq), 3)
        self.assertEqual(self.my_stack.top(), 3)

    def test_pop(self):
        self.assertEqual(self.my_stack.pop(), 3)
        self.assertEqual(len(self.my_stack.dq), 2)
        self.assertEqual(self.my_stack.pop(), 2)

    def test_empty(self):
        self.my_stack = MyStack()
        self.assertTrue(self.my_stack.empty())
        self.my_stack.push(1)
        self.assertTrue(not self.my_stack.empty())


class MyCircularQueue:
    """
    设计循环队列（LeetCode 622）
    描述：设计你的循环队列实现。循环队列是一种线性数据结构，其操作表现基于FIFO原则并且队尾被连接在队首之后以形成一个循环
    """

    def __init__(self, capacity: int):
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = capacity

    def en_queue(self, value):
        if self.is_full():
            return False
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def de_queue(self) -> int:
        if self.is_empty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def front(self) -> int | None:
        if self.is_empty():
            return -1
        return self.queue[self.head]

    def rear(self) -> bool | None:
        if self.is_empty():
            return False
        # 因为tail和size相等，所以是self.tail - 1
        return self.queue[(self.tail - 1) % self.capacity]

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity


class TestMyCircularQueue(unittest.TestCase):
    def setUp(self):
        self.my_circular_queue = MyCircularQueue(5)
        self.my_circular_queue.en_queue(1)
        self.my_circular_queue.en_queue(2)
        self.my_circular_queue.en_queue(3)

    def test_en_queue(self):
        self.my_circular_queue.en_queue(4)
        self.my_circular_queue.en_queue(5)
        self.assertEqual(self.my_circular_queue.front(), 1)
        self.assertEqual(self.my_circular_queue.rear(), 5)
        self.assertTrue(self.my_circular_queue.is_full())

    def test_de_queue(self):
        self.my_circular_queue.de_queue()
        self.assertEqual(self.my_circular_queue.front(), 2)

    def test_is_empty(self):
        self.assertFalse(self.my_circular_queue.is_empty())
        self.my_circular_queue.de_queue()
        self.my_circular_queue.de_queue()
        self.my_circular_queue.de_queue()
        self.assertTrue(self.my_circular_queue.is_empty())


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
        :param temperature:
        :return:
        """
        n = len(temperature)
        res = n * [0]
        for i in range(n):
            for j in range(i + 1, n):
                if temperature[j] > temperature[i]:
                    res[i] = j - i
                    break
        return res

    @staticmethod
    def daily_temperatures1(temperature: list[int]) -> list[int]:
        """
        使用单调栈解法
        :param temperature:
        :return:
        """
        n = len(temperature)
        res = [0] * n
        stack = []
        for i in range(n):
            while stack and temperature[i] > temperature[stack[-1]]:
                top_index = stack.pop()
                res[top_index] = i - top_index
            stack.append(i)
        return res

    @staticmethod
    def next_greater_element(nums: list[int]) -> list[int]:
        """
        下一个更大元素 II（LeetCode 503）
        数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。
        示例 1:
        输入: nums = [1,2,1]
        输出: [2,-1,2]
        解释: 第一个 1 的下一个更大的数是 2；
        数字 2 找不到下一个更大的数；
        第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

        示例 2:
        输入: nums = [1,2,3,4,3]
        输出: [2,3,4,-1,4]
        提示:
        1 <= nums.length <= 104
        -109 <= nums[i] <= 109

        :param nums:
        :return:
        """
        n = len(nums)
        res = [-1] * n
        stack = []
        # 这里是一个技巧，对于循环数组，使用数组双倍长度
        for i in range(n * 2):
            current_index = i % n
            # 因为是元素，所以只需要比较当前元素和栈顶索引对应的元素即可
            while stack and nums[current_index] > nums[stack[-1]]:
                # 栈顶存储的都是比当前元素大的元素的索引
                top = stack.pop()
                res[top] = nums[current_index]
            stack.append(current_index)
        return res

    @staticmethod
    def remove_duplicates(string: str) -> str:
        """
        删除字符串中的所有相邻重复项（LeetCode 1047）
        给出由小写字母组成的字符串 s，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
        在 s 上反复执行重复项删除操作，直到无法继续删除。
        在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

        示例：
        输入："abbaca"
        输出："ca"
        解释：
        例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。
        之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

        提示：
        1 <= s.length <= 105
        s 仅由小写英文字母组成。

        :param string:
        :return:
        """
        stack = []
        for ch in string:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)

    @staticmethod
    def is_valid(string: str) -> bool:
        """
        有效的括号（LeetCode 20）
        给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
        有效字符串需满足：
        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
        每个右括号都有一个对应的相同类型的左括号。
        示例 1：
        输入：s = "()"
        输出：true

        示例 2：
        输入：s = "()[]{}"
        输出：true

        示例 3：
        输入：s = "(]"
        输出：false

        示例 4：
        输入：s = "([])"
        输出：true

        :return:
        """
        # 奇数长度肯定不匹配
        if len(string) % 2 != 0:
            return False
        m = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in string:
            if ch not in m:  # 不是右括号(是左括号)则进栈
                stack.append(ch)
            elif not stack or m[ch] != stack.pop():  # 栈不为空说明匹配不完,栈顶[全都是左括号]对应的右括号不能匹配
                return False
        return not stack


class TestDailyTemperature(unittest.TestCase):

    def setUp(self):
        self.temps = [73, 74, 75, 71, 69, 72, 76, 73]
        self.dt = DailyTemperature()

    def test_daily_temperatures(self):
        self.assertEqual(DailyTemperature.daily_temperatures(self.temps), [1, 1, 4, 2, 1, 1, 0, 0])

    def test_daily_temperatures1(self):
        self.assertEqual(DailyTemperature.daily_temperatures1(self.temps), [1, 1, 4, 2, 1, 1, 0, 0])

    def test_next_greater_element(self):
        self.assertEqual(DailyTemperature.next_greater_element([1, 2, 3, 4, 3]), [2, 3, 4, -1, 4])

    def test_remove_duplicates(self):
        self.assertEqual(DailyTemperature.remove_duplicates('122433'), '14')

    def test_is_valid1(self):
        self.assertTrue(DailyTemperature.is_valid('()[]{}'))

    def test_is_valid2(self):
        self.assertFalse(DailyTemperature.is_valid('(]{}'))

    def test_is_valid3(self):
        self.assertTrue(DailyTemperature.is_valid('()'))

    def test_is_valid4(self):
        self.assertTrue(DailyTemperature.is_valid('([]{})'))

    def test_is_valid5(self):
        self.assertFalse(DailyTemperature.is_valid('())'))

    def test_is_valid6(self):
        self.assertTrue(DailyTemperature.is_valid('({[]})'))

    def test_is_valid7(self):
        self.assertFalse(DailyTemperature.is_valid(')('))

    def test_is_valid8(self):
        self.assertFalse(DailyTemperature.is_valid('[}'))

    def test_is_valid9(self):
        self.assertFalse(DailyTemperature.is_valid('}{'))


from collections import deque

"""
    滑动窗口最大值 (LeetCode 239)
    给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
    你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。返回 滑动窗口中的最大值 。

    示例 1：
    输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
    输出：[3,3,5,5,6,7]
    解释：
    滑动窗口的位置                   最大值
    -------------------------      -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7
    示例 2：
    输入：nums = [1], k = 1
    输出：[1]

    提示：
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    1 <= k <= nums.length
"""


def max_sliding_window1(nums, k):
    """
    滑动窗口暴力解法
    :param nums:
    :param k:
    :return:
    """
    n = len(nums)
    result = []
    for i in range(n - k + 1):  # 遍历所有窗口的起始位置
        current_max = -float('inf')
        # 遍历窗口内的k个元素，找最大值
        for j in range(i, i + k):
            current_max = max(current_max, nums[j])
        result.append(current_max)
    return result


def max_sliding_window(nums, k):
    """
    滑动窗口单调队列解法
    :param nums:
    :param k:
    :return:
    """
    if not nums:
        return []
    window, res = [], []
    for i, x in enumerate(nums):
        # i >= k表示窗口至少有K个元素满窗口了
        if i >= k and window[0] <= i - k:  # window[0] <= i - k 是落后于窗口的左边界
            # 剔除最左边的
            window.pop(0)
        while window and nums[window[-1]] <= x:  # 把比x小的所有元素都可以剔除,因为我们要求是要最大值
            window.pop()
        window.append(i)   # 首先window里存的是list元素索引
        if i - k + 1 >= 0:  # 窗口满足有K个元素
            res.append(nums[window[0]])
    return res


class TestMaxSlidingWindow(unittest.TestCase):
    def setUp(self):
        self.nums = [1, 3, -1, -3, 5, 3, 6, 7]
        self.k = 3

    def test_max_sliding_window1(self):
        self.assertEqual(max_sliding_window1(self.nums, 3), [3, 3, 5, 5, 6, 7])

    def test_max_sliding_window(self):
        self.assertEqual(max_sliding_window(self.nums, 3), [3, 3, 5, 5, 6, 7])


class TrapSolution:
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
        解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

    示例 2：
    输入：height = [4,2,0,3,2,5]
    输出：9
    """

    @staticmethod
    def trap1(height: list[int]) -> int:
        """
        暴力解法
        :param height:
        :return:
        """
        ans = 0
        n = len(height)
        for i in range(n):
            # 计算height[i]左边的最大值
            max_left = 0
            for j in range(i):
                if height[j] > max_left:
                    max_left = height[j]
            # 计算height[i]右边的最大值
            max_right = 0
            for j in range(i + 1, n):
                if height[j] > max_right:
                    max_right = height[j]
            # 计算储水量(木桶效应，装水的多少由最短的那个木板决定)
            water = min(max_left, max_right) - height[i]
            if water > 0:
                ans += water
        return ans

    @staticmethod
    def trap2(height: list[int]) -> int:
        """
        单调栈解法
        思路：
        1. 使用一个栈（列表），用于存储柱子的下标，栈中保存的下标对应的柱子高度保持单调递减。
        2. 遍历数组，对于当前柱子：
            - 如果当前柱子高度大于栈顶柱子，则说明存在“凹槽”
              —— 弹出栈顶元素，设为 mid_index，此时栈顶的下一个元素 left_index（若存在）就是凹槽左边界，
              —— 当前下标 i 是右边界。可计算接水高度 = min(height[left_index], height[i]) - height[mid_index]，
              —— 凹槽宽度 = i - left_index - 1。
              累加面积（雨水量）到答案中。
            - 否则直接将当前下标入栈。
        3. 返回累加的雨水总量。

        时间复杂度 O(n)：每个元素最多进栈和出栈一次。
        空间复杂度 O(n)：最坏情况下栈中存储所有下标。
        :param height:
        :return:
        """
        n = len(height)
        ans = 0  # 用于累计雨水总量
        stack = []  # 栈，用于存储柱子的下标

        # 遍历所有柱子的下标
        for i in range(n):
            # 当栈不为空且当前柱子的高度大于栈顶柱子高度时，说明出现了一个可接水的凹槽
            while stack and height[i] > height[stack[-1]]:
                # 弹出栈顶，下标对应的柱子即为凹槽的底部(这是一个逻辑问题，因为上面while循环条件是height[i] > height[stack[-1]]，所以栈顶元素必然是最小的)
                mid_index = stack.pop()
                # 如果栈为空，则说明没有左边界，无法形成凹槽，退出循环
                if not stack:
                    break
                left_index = stack[-1]  # 当前新的栈顶即为凹槽左边界下标
                # 计算凹槽宽度：右边界 i 与左边界 left_index 之间的距离减 1
                width = i - left_index - 1
                # 计算能接雨水的高度：左右两边边界的较小值减去凹槽底部高度
                bounded_height = min(height[left_index], height[i]) - height[mid_index]
                # 将该凹槽区域的雨水量累加到结果中
                ans += width * bounded_height
            # 当前下标入栈，等待后续处理
            stack.append(i)

        return ans

    @staticmethod
    def trap3(height: list[int]) -> int:
        """
        双指针解法
          3  |_                    ___
          2  |_        ___        |  |___   ___
          1  |_  ___  |  |___   __|  |  |__|  |___
             |__|__|__|__|__|__|__|__|__|__|__|__|
              0  1  0  2  1  0  1  3  2  1  2  1
        :param height:
        :return:
        """
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # 这个else里的条件是(left_max >= height[left]) < height[right],
                    # 这样就必然在height[left]处形成凹槽，而
                    # height[left]处的储水量 = min(left_max, height[left]) - height[left]
                    #                      = left_max - height[left]
                    ans += left_max - height[left]
                # left指针向右移动
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                # right指针左移动
                right -= 1
        return ans


class TestTrapSolution(unittest.TestCase):
    def setUp(self):
        self.height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    def test_trap1(self):
        self.assertEqual(TrapSolution.trap1(self.height), 6)

    def test_trap2(self):
        self.assertEqual(TrapSolution.trap2(self.height), 6)

    def test_trap3(self):
        self.assertEqual(TrapSolution.trap3(self.height), 6)


class CalculaterSolution:
    """
    基本计算器 II（LeetCode 227）
    给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。整数除法仅保留整数部分。
    你可以假设给定的表达式总是有效的。所有中间结果将在 [-231, 231 - 1] 的范围内。
    注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval()。

    示例 1：
    输入：s = "3+2*2"
    输出：7

    示例 2：
    输入：s = " 3/2 "
    输出：1

    示例 3：
    输入：s = " 3+5 / 2 "
    输出：5

    :type s: str
    :rtype: int
    """

    @staticmethod
    def calculate1(s: str) -> int:

        # 定义一个函数返回运算符的优先级
        def precedence(op: str) -> int:
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            return 0

        # 定义一个函数，根据运算符对两个操作数进行计算
        def apply_operator(a: int, b: int, op: str) -> int:
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            elif op == '/':
                # 使用 int(a / b) 来实现向零截断的整数除法
                return int(a / b)

        # 去掉所有空格，简化处理
        s = s.replace(' ', '')
        num_stack = []  # 存放数字的栈
        op_stack = []  # 存放运算符的栈

        i = 0
        n = len(s)
        while i < n:
            ch = s[i]
            if ch.isdigit():
                # 如果遇到数字，可能是多位数，连续读取数字
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                # 将读到的数字压入数字栈
                num_stack.append(num)
                # 这里 continue 跳过后面的 i+=1，因为在内层循环中已自增
                continue
            else:
                # 当前字符为运算符：+ - * /
                # 当 op_stack 非空且栈顶运算符优先级大于或等于当前运算符，
                # 则先弹出栈顶运算符并计算对应结果
                while op_stack and precedence(op_stack[-1]) >= precedence(ch):
                    op = op_stack.pop()  # 弹出运算符
                    b = num_stack.pop()  # 弹出数字栈的右操作数
                    a = num_stack.pop()  # 弹出数字栈的左操作数
                    # 将计算结果入栈
                    num_stack.append(apply_operator(a, b, op))
                # 将当前运算符入栈
                op_stack.append(ch)
            i += 1

        # 遍历结束后，可能 op_stack 中还有剩余运算符，依次计算
        while op_stack:
            op = op_stack.pop()
            b = num_stack.pop()
            a = num_stack.pop()
            num_stack.append(apply_operator(a, b, op))

        # 数字栈中最后的结果即为最终答案
        return num_stack[0]


class TestCalculaterSolution(unittest.TestCase):
    def setUp(self):
        self.string = " 3+5 / 2 "

    def test_calculate1(self):
        self.assertEqual(CalculaterSolution.calculate1(self.string), 5)


import heapq


class KthLargest:
    """
    数据流中的第K大元素
    使用最小堆
    """

    def __init__(self, k, nums: list[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # 堆中永远只保留K个元素,堆顶是K个中最小的,
        # 往后数据流中的的新元素只要比堆顶大,就替换堆顶元素即可
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:  # 替换比堆顶大的元素,因为堆顶是最小的
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap.val)
        return self.min_heap[0]  # 返回堆顶


def max_sliding_window(nums, k):
    if not nums:
        return []
    window, res = [], []
    for i, x in enumerate(nums):
        # i >= k表示窗口至少有K个元素满窗口了
        if i >= k and window[0] <= i - k:  # window[0] <= i - k 是落后于窗口的左边界
            # 剔除最左边的
            window.pop(0)
        while window and nums[window[-1]] <= x:  # 把比x小的所有元素都可以剔除,因为我们要求是要最大值
            window.pop()
        window.append(i)   # 首先window里存的是list元素索引
        if i >= k - 1:  # 窗口满足有K个元素
            res.append(nums[window[0]])
    return res






