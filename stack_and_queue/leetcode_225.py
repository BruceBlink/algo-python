import unittest


class MyQueue:
    """
    用双栈实现队列（LeetCode 225）
    描述：请你仅使用两个栈实现一个先入先出（FIFO）的队列，并支持普通队列的全部操作（push，pop，peek，empty）。
    """

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, val: int):
        self.input.append(val)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
            return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output


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