import unittest


class MyCircularQueue:
    """
    设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

    循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

    你的实现应该支持如下操作：

    MyCircularQueue(k): 构造器，设置队列长度为 k 。
    Front: 从队首获取元素。如果队列为空，返回 -1 。
    Rear: 获取队尾元素。如果队列为空，返回 -1 。
    enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
    deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
    isEmpty(): 检查循环队列是否为空。
    isFull(): 检查循环队列是否已满。
    示例：

    MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
    circularQueue.enQueue(1);  // 返回 true
    circularQueue.enQueue(2);  // 返回 true
    circularQueue.enQueue(3);  // 返回 true
    circularQueue.enQueue(4);  // 返回 false，队列已满
    circularQueue.Rear();  // 返回 3
    circularQueue.isFull();  // 返回 true
    circularQueue.deQueue();  // 返回 true
    circularQueue.enQueue(4);  // 返回 true
    circularQueue.Rear();  // 返回 4


    提示：
    所有的值都在 0 至 1000 的范围内；
    操作数将在 1 至 1000 的范围内；
    请不要使用内置的队列库。

    这里有两种常见的指针表示方法：
    1. front 指向队头元素，rear 指向队尾元素。这种情况下，为了区分空和满，
       通常会牺牲一个存储单元，或者额外使用一个计数器来记录队列中的元素数量。
    2. front 指向队头元素，rear 指向队尾的下一个空位置。这种情况下，当 front == rear 时表示队列为空，
       当 (rear + 1) % capacity == front 时表示队列已满。这种方法不需要额外的计数器或牺牲空间，是比较简洁的一种。
    我们采用第二种方法来实现，即 front 指向队头，rear 指向队尾的下一个位置。

    """

    def __init__(self, capacity: int):
        """
        初始化
        """
        # 使用一个固定大小的列表来存储队列元素
        self.queue = [None] * capacity
        # 队列的容量
        self.capacity = capacity
        # 队头指针，指向队列的第一个元素
        self.head = 0
        # 队尾指针，指向队列最后一个元素的下一个位置
        self.tail = 0
        # 当前队列中的元素数量
        self.size = 0

    def en_queue(self, val) -> bool:
        """
        入队列
        """
        # 队列已满则无法插入
        if self.is_full():
            return False
        # 在队尾指针指向的位置插入元素
        self.queue[self.tail] = val
        # 队尾指针向右移动，使用取模运算实现循环
        self.tail = (self.tail + 1) % self.capacity
        # 队列的元素个数加1
        self.size += 1
        return True

    def de_queue(self) -> bool:
        """
        出队列
        """
        # 如果队列为空，无法出队
        if self.is_empty():
            return False
        # 将队首元素设置为None
        self.queue[self.head] = None
        # 对首向右移动，使用取模运算实现循环
        self.head = (self.head + 1) % self.capacity
        # 队列的元素个数减一
        self.size -= 1
        return True

    def front(self) -> int:
        """
        获取队首元素
        """
        if self.is_empty():
            return -1
        # 返回队首指向的元素
        return self.queue[self.head]

    def rear(self) -> int | None:
        """
        获取队尾元素
        """
        if self.is_empty():
            return -1
        # 队尾指针指向队尾的下一个位置，所以队尾元素在 (rear - 1 + capacity) % capacity
        # 加上 capacity 是为了处理 rear = 0 的情况
        return self.queue[(self.tail - 1 + self.capacity) % self.capacity]

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
