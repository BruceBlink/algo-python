class MinStack:
    """
    设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
    实现 MinStack 类:
    MinStack() 初始化堆栈对象。
    void push(int val) 将元素val推入堆栈。
    void pop() 删除堆栈顶部的元素。
    int top() 获取堆栈顶部的元素。
    int getMin() 获取堆栈中的最小元素。

    示例 1:
    输入：
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    输出：
    [null,null,null,null,-3,null,0,-2]

    解释：
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> 返回 -3.
    minStack.pop();
    minStack.top();      --> 返回 0.
    minStack.getMin();   --> 返回 -2.


    提示：
    -231 <= val <= 231 - 1
    pop、top 和 getMin 操作总是在 非空栈 上调用
    push, pop, top, and getMin最多被调用 3 * 104 次
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 数据栈，存储所有元素
        self.data_stack = []
        # 最小栈，存储每一步的最小元素
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Pushes the element val onto the stack.
        """
        # 将元素压入数据栈
        self.data_stack.append(val)

        # 更新最小栈：
        # 如果最小栈为空，或者当前元素小于等于最小栈的栈顶元素，则将当前元素压入最小栈
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # 否则，将最小栈的栈顶元素再次压入最小栈
            # 这样保证 min_stack 的栈顶始终是 data_stack 中对应位置的最小值
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        """
        Removes the element on top of the stack.
        """
        # 同时从数据栈和最小栈弹出元素
        if self.data_stack:  # 检查数据栈是否为空，防止 pop 空栈
            self.data_stack.pop()
            self.min_stack.pop()

    def top(self) -> int | None:
        """
        Gets the top element of the stack.
        """
        # 返回数据栈的栈顶元素
        if self.data_stack:  # 检查数据栈是否为空
            return self.data_stack[-1]
        # 根据题目要求，pop 或 top 一个空栈的行为可能需要特殊处理，这里返回None或抛出异常
        return None  # 或者 raise IndexError("top from empty stack")

    def get_min(self) -> int | None:
        """
        Retrieves the minimum element in the stack.
        """
        # 返回最小栈的栈顶元素
        if self.min_stack:  # 检查最小栈是否为空
            return self.min_stack[-1]
        # 如果栈为空，没有最小元素，根据题目要求处理
        return None  # 或者 raise IndexError("getMin from empty stack")


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
