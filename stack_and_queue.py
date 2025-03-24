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
    描述：给定一个温度列表，要生成一个结果列表，结果列表的每个元素表示需要等多少天才能遇到更高的温度。如果之后都不会升高，就用0代替。
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
        描述：给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），返回数组中每个元素的下一个更大元素。

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
        在 s 上反复执行重复项删除操作，直到无法继续删除。在完成所有重复项删除操作后返回最终的字符串。
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
            if ch in m:
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
