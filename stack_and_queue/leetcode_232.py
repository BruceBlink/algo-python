import unittest
from collections import deque
from typing import Any


class MyStack:
    """
    请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。
    实现 MyStack 类：
    void push(int x) 将元素 x 压入栈顶。
    int pop() 移除并返回栈顶元素。
    int top() 返回栈顶元素。
    boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。

    注意：

    你只能使用队列的标准操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
    你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
    示例：

    输入：
    ["MyStack", "push", "push", "top", "pop", "empty"]
    [[], [1], [2], [], [], []]
    输出：
    [null, null, null, 2, 2, false]

    解释：
    MyStack myStack = new MyStack();
    myStack.push(1);
    myStack.push(2);
    myStack.top(); // 返回 2
    myStack.pop(); // 返回 2
    myStack.empty(); // 返回 False

    提示：

    1 <= x <= 9
    最多调用100 次 push、pop、top 和 empty
    每次调用 pop 和 top 都保证栈不为空
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 使用一个 deque 来模拟队列
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # 将新元素加入队列尾部
        self.queue.append(x)

        # 将新加入元素之前的所有元素，从队列头部取出，再添加到队列尾部
        # 这样，新加入的元素就会被“旋转”到队列的头部
        # 循环次数是队列当前长度减 1
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> Any | None:
        """
        Removes the element on top of the stack and returns that element.
        """
        # 由于 push 操作保证了队列头部是栈顶元素，直接从头部弹出即可
        if self.empty():
            # 根据题目要求，pop 空栈的行为可能需要特殊处理，这里假设不会弹出空栈
            # 或者可以抛出异常
            return None  # 或者 raise IndexError("pop from empty stack")
        return self.queue.popleft()

    def top(self) -> Any | None:
        """
        Get the top element.
        """
        # 由于 push 操作保证了队列头部是栈顶元素，直接查看头部元素即可
        if self.empty():
            # 同样，处理空栈情况
            return None  # 或者 raise IndexError("top from empty stack")
        return self.queue[0]  # deque 支持通过索引访问头部元素 (O(1))

    def empty(self) -> bool:
        """
        Returns true if the stack is empty, false otherwise.
        """
        # 检查队列是否为空
        return len(self.queue) == 0


class TestMyStack(unittest.TestCase):
    def setUp(self):
        self.my_stack = MyStack()
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.my_stack.push(3)

    def test_push_and_top(self):
        self.assertEqual(len(self.my_stack.queue), 3)
        self.assertEqual(self.my_stack.top(), 3)

    def test_pop(self):
        self.assertEqual(self.my_stack.pop(), 3)
        self.assertEqual(len(self.my_stack.queue), 2)
        self.assertEqual(self.my_stack.pop(), 2)

    def test_empty(self):
        self.my_stack = MyStack()
        self.assertTrue(self.my_stack.empty())
        self.my_stack.push(1)
        self.assertTrue(not self.my_stack.empty())
