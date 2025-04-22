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
        if not self.min_stack or self.stack[-1] <= self.min_stack[-1]:
            self.min_stack.append(num)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.min_stack.pop()

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
