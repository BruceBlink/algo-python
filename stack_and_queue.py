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
            # 判断key(右括号)是否在字典中，左括号进栈，右括号作为字典的key
            if ch in m:
                # 判断左右括号是否匹配，如果匹配就出栈，栈为空则说明匹配完全
                if not stack or stack.pop() != m[ch]:
                    return False
            else:
                stack.append(ch)
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
    window = deque()  # 保存索引，队列元素对应值递减
    result = []
    for i, num in enumerate(nums):
        # 移除超出窗口左侧的队首元素
        while window and window[0] < i - k + 1:
            window.popleft()
        # 维护队列递减：移除队尾小于当前值的元素
        while window and nums[window[-1]] <= num:
            window.pop()
        window.append(i)
        # 当窗口形成时（i >= k-1），记录队首元素
        if i >= k - 1:
            result.append(nums[window[0]])
    return result


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

        输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
        输出：6
        解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

    示例 2：
    输入：height = [4,2,0,3,2,5]
    输出：9
    """

    @staticmethod
    def trap1(height: list[int]):
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


class TestTrapSolution(unittest.TestCase):
    def setUp(self):
        self.height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    def test_trap1(self):
        self.assertEqual(TrapSolution.trap1(self.height), 6)
