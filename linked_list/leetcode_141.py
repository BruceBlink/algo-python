"""
141. 环形链表
给你一个链表的头节点 head ，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
如果链表中存在环 ，则返回 true 。 否则，返回 false 。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

提示：

链表中节点的数目范围是 [0, 10^4]
-10^5 <= Node.val <= 10^5
pos 为 -1 或者链表中的一个 有效索引 。
"""
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    # 如果链表为空或只有一个节点，不可能有环
    if head is None or head.next is None:
        return False

    # 初始化快慢指针，都指向头节点
    slow = head
    fast = head

    # 当快指针和它的下一个节点不为空时循环
    # 这个条件确保 fast.next 和 fast.next.next 的访问是安全的
    while fast is not None and fast.next is not None:
        # 慢指针移动一步
        slow = slow.next
        # 快指针移动两步
        fast = fast.next.next

        # 检查快慢指针是否相遇
        if slow == fast:
            return True  # 相遇，说明有环

    # 循环结束仍未相遇，说明快指针到达了链表末尾，没有环
    return False


class TestHasCycle(unittest.TestCase):

    def test_has_cycle(self):
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
        self.assertFalse(has_cycle(node1))

    def test_has_cycle1(self):
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        head2 = ListNode(-1)
        # [-1, 3, 2, 4, 3]
        head2.next = node3
        node3.next = node2
        node2.next = node4
        node4.next = node3
        self.assertTrue(has_cycle(head2))
