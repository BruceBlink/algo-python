from typing import List, Any


class MinStack:
    """
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