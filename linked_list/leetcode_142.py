"""
142. 环形链表II
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
不允许修改 链表。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：

输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：

输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。


提示：

链表中节点的数目范围在范围 [0, 104] 内
-10^5 <= Node.val <= 1^05
pos 的值为 -1 或者链表中的一个有效索引
"""
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detect_cycle(head: ListNode) -> None | ListNode:
    # 如果链表为空或只有一个节点，不可能有环
    if head is None or head.next is None:
        return None

    slow = head
    fast = head

    # 第一阶段：检测环
    while fast is not None and fast.next is not None:
        slow = slow.next  # 慢指针走一步
        fast = fast.next.next  # 快指针走两步

        # 如果相遇，说明有环，中断循环进入第二阶段
        if slow == fast:
            break

    # 如果循环是正常结束 (fast 或 fast.next 为 None)，说明没有环
    if fast is None or fast.next is None:
        return None

    # 第二阶段：寻找环的入口点
    # 将慢指针重新指向链表头部
    slow = head

    # 快慢指针同时以一步的速度移动，直到再次相遇
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # 相遇点就是环的入口点
    return slow


# Helper function to create a linked list from a list of values and a position for cycle
def create_linked_list_with_cycle(values: list, pos: int) -> ListNode:
    if not values:
        return None

    nodes = [ListNode(val) for val in values]

    # Link nodes sequentially
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Create the cycle if pos is valid
    if pos != -1 and 0 <= pos < len(nodes):
        nodes[-1].next = nodes[pos]

    return nodes[0]


# Unit tests using unittest.TestCase
class TestDetectCycle(unittest.TestCase):

    def test_example_1(self):
        # Input: [3,2,0,-4], pos = 1
        values = [3, 2, 0, -4]
        pos = 1
        head = create_linked_list_with_cycle(values, pos)

        # The expected cycle start node is the node at index 'pos'
        expected_start_node = None
        if head and pos != -1:
            # Traverse to the node at index pos
            current = head
            for _ in range(pos):
                current = current.next
            expected_start_node = current

        result = detect_cycle(head)

        # Assert that the returned node is the expected start node object
        self.assertEqual(result, expected_start_node)
        # Optional: Also check the value just for clarity in test output if assertion fails
        if result:
            self.assertEqual(result.val, expected_start_node.val)

    def test_example_2(self):
        # Input: [1,2], pos = 0
        values = [1, 2]
        pos = 0
        head = create_linked_list_with_cycle(values, pos)

        expected_start_node = None
        if head and pos != -1:
            current = head
            for _ in range(pos):
                current = current.next
            expected_start_node = current

        result = detect_cycle(head)

        self.assertEqual(result, expected_start_node)
        if result:
            self.assertEqual(result.val, expected_start_node.val)

    def test_example_3(self):
        # Input: [1], pos = -1 (no cycle)
        values = [1]
        pos = -1
        head = create_linked_list_with_cycle(values, pos)

        expected_start_node = None  # No cycle expected

        result = detect_cycle(head)

        self.assertIsNone(result)  # Expecting None

    def test_no_cycle(self):
        # Input: [1,2,3], pos = -1 (no cycle)
        values = [1, 2, 3]
        pos = -1
        head = create_linked_list_with_cycle(values, pos)

        expected_start_node = None  # No cycle expected

        result = detect_cycle(head)

        self.assertIsNone(result)  # Expecting None

    def test_empty_list(self):
        # Input: [], pos = -1 (empty list, no cycle)
        values = []
        pos = -1
        head = create_linked_list_with_cycle(values, pos)

        expected_start_node = None  # No cycle expected

        result = detect_cycle(head)

        self.assertIsNone(result)  # Expecting None
