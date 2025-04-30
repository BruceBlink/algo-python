"""
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
示例 1：

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]


提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    # 创建一个哑节点，指向链表头部，方便处理删除头节点的情况
    dummy_head = ListNode(0)
    dummy_head.next = head

    # 初始化快慢指针，都指向哑节点
    fast = dummy_head
    slow = dummy_head

    # 快指针先行 n+1 步
    # 移动 n+1 步是为了让 slow 指针最终停在要删除节点的前一个节点
    for _ in range(n + 1):
        # 注意这里通常题目保证 n 是有效的，如果 n 可能无效，需要检查 fast 是否为 None
        fast = fast.next

    # 快慢指针同时移动，直到快指针到达链表末尾 (None)
    while fast is not None:
        fast = fast.next
        slow = slow.next

    # 此时，slow 指针指向要删除节点的 前一个 节点
    # 删除慢指针指向的下一个节点
    slow.next = slow.next.next

    # 返回哑节点的下一个节点，即删除后的新链表头部
    return dummy_head.next


class TestRemoveNthFromEnd(unittest.TestCase):

    def test_remove_nth_from_end(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node5 = ListNode(5)
        node6 = ListNode(6)
        # [1, 3, 6, 5, 2]
        node1.next = node3
        node3.next = node6
        node6.next = node5
        node5.next = node2
        new_node = remove_nth_from_end(node1, 2)
        # new_node_val = [1, 3, 6, 5, 2]
        self.assertEqual(node1, new_node)

    def test_remove_nth_from_end1(self):
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        head2 = ListNode(-1)
        node5 = ListNode(5)
        # [-1, 3, 2, 4, 5]
        head2.next = node3
        node3.next = node2
        node2.next = node4
        node4.next = node5
        new_node = remove_nth_from_end(head2, 3)
        # [-1, 3, 4, 5]
        self.assertEqual(head2, new_node)
