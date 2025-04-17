from __future__ import annotations


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: None | ListNode = None


def reverse_list(head: ListNode) -> ListNode:
    """
    反转链表
    :param head:
    :return:
    """
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev


def reverse_list1(head: ListNode) -> ListNode:
    """
    反转链表
    :param head:
    :return:
    """
    cur, prev = head, None
    while cur:
        next_node = cur.next  # 保存下一个节点
        cur.next = prev  # 反转当前节点的指针
        prev = cur  # prev移动到当前节点
        cur = next_node  # cur移动到下一个节点
    return prev


def swap_pairs(head: ListNode) -> ListNode:
    """
    链表节点交换相邻节点(迭代法)
    :param head:
    :return:
    """
    dummy = ListNode(0, head)  # 创建虚拟头节点指向 head
    prev = dummy
    while prev.next and prev.next.next:  # 确保至少有2个节点
        first = prev.next
        second = prev.next.next

        # 交换相邻节点
        prev.next = second
        first.next = second.next
        second.next = first

        # 移动指针(循环的进行条件)
        prev = first

    return dummy.next  # 新链表的头节点


def swap_pairs_recursion(head: ListNode) -> ListNode:
    """
    链表节点交换相邻节点(递归法)
    :param head:
    :return:
    """
    if not head or not head.next:  # 链表为空或者只有一个节点
        return head

    first = head
    second = head.next
    # 交换first和second, 然后递归处理剩余所有的节点
    first.next = swap_pairs(second.next)
    second.next = first

    return second


def has_cycle(head: ListNode) -> bool:
    """
    判断链表是否有环(leetcode 141)
    快慢指针法
    :param head:
    :return:
    """
    fast = slow = head
    while fast and slow and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            return True
    return False


def has_cycle(head: ListNode) -> bool:
    """
    使用hashset
    :param head:
    :return:
    """
    visited = set()
    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next  # 步进条件
    return False
