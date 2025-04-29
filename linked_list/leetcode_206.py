"""
206. 反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：


输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]


提示：

链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000
"""
from __future__ import annotations

import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    prev = None  # 前一个节点，初始化为 None
    curr = head  # 当前节点，从头节点开始

    # 循环直到当前节点为空
    while curr:
        """
        迭代法
        """
        # 1. 保存当前节点的下一个节点，以免改变指向后找不到它
        next_node = curr.next

        # 2. 改变当前节点的 next 指向，指向前一个节点
        curr.next = prev

        # 3. 移动 prev 指针：将当前节点设为下一个循环的前一个节点
        prev = curr

        # 4. 移动 curr 指针：移到之前保存的下一个节点
        curr = next_node

    # 循环结束后，prev 指向原链表的最后一个节点，即反转后链表的头节点
    return prev


def reverse_list1(head: ListNode) -> ListNode:
    prev = None  # 前一个节点，初始化为 None
    curr = head  # 当前节点，从头节点开始

    # 循环直到当前节点为空
    while curr is not None:
        curr.next, prev, curr = prev, curr, curr.next

    # 循环结束后，prev 指向原链表的最后一个节点，即反转后链表的头节点
    return prev


def reverse_list2(head: ListNode) -> ListNode | None:
    """
    递归法
    """
    # 基本情况：链表为空或只有一个节点，直接返回 head
    if head is None or head.next is None:
        return head

    # 递归调用：反转剩余链表（从 head.next 开始的部分）
    # new_head 是反转后的剩余链表的头节点
    new_head = reverse_list2(head.next)

    # 连接节点：
    # head.next 原来是链表的第二个节点，现在是反转后剩余链表的尾节点
    # 让这个尾节点的 next 指向原头节点 head
    head.next.next = head

    # 让原头节点 head 的 next 指向 None，因为它现在是整个反转链表的尾节点
    head.next = None

    # 返回反转后的整个链表的头节点 (这个头节点在递归调用 new_head = ... 时已经确定并层层传递)
    return new_head


class TestReverseList(unittest.TestCase):

    def setUp(self):
        self.head1 = ListNode(1)
        self.head1.next = ListNode(2)
        self.head1.next.next = ListNode(3)
        self.head1.next.next.next = ListNode(4)
        self.head1.next.next.next.next = ListNode(5)
        self.head2 = ListNode(5)
        self.head2.next = ListNode(4)
        self.head2.next.next = ListNode(3)
        self.head2.next.next.next = ListNode(2)
        self.head2.next.next.next.next = ListNode(1)

    def test_reverse_list(self):
        temp = reverse_list(self.head1)
        self.assertEqual(self.head2.val, temp.val)
        self.assertEqual(self.head2.next.val, temp.next.val)
        self.assertEqual(self.head2.next.next.val, temp.next.next.val)
        self.assertEqual(self.head2.next.next.next.val, temp.next.next.next.val)
        self.assertEqual(self.head2.next.next.next.next.val, temp.next.next.next.next.val)

    def test_reverse_list1(self):
        temp = reverse_list1(self.head1)
        self.assertEqual(self.head2.val, temp.val)
        self.assertEqual(self.head2.next.val, temp.next.val)
        self.assertEqual(self.head2.next.next.val, temp.next.next.val)
        self.assertEqual(self.head2.next.next.next.val, temp.next.next.next.val)
        self.assertEqual(self.head2.next.next.next.next.val, temp.next.next.next.next.val)

    def test_reverse_list3(self):
        temp = reverse_list2(self.head1)
        self.assertEqual(self.head2.val, temp.val)
        self.assertEqual(self.head2.next.val, temp.next.val)
        self.assertEqual(self.head2.next.next.val, temp.next.next.val)
        self.assertEqual(self.head2.next.next.next.val, temp.next.next.next.val)
        self.assertEqual(self.head2.next.next.next.next.val, temp.next.next.next.next.val)
